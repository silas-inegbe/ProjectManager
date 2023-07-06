from django.shortcuts import render
from .models import Project,ProjectTeamMember, Issue , Risk,ProjectManager ,Task ,Milestone
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import models
from .serializers import( ProjectCreateSerializer,ProjectDetailSerializer,ProjectListSerializer,
                         ProjectTeamMemberSerializer,ProjectTeamMemberListSerializer,
                         ProjectUpdateSerializer, IssueUpdateSerializer, TaskSerializer,IssueCreateSerializer,IssueSerializer, ProjectMilestoneSerializer,TaskListSerializer,TaskCreateSerializer,TaskUpdateSerializer,ProjectTeamRemoveSerializer,ProjectTeamAddSerializer,ProjectTeamCreateSerializer)
from .permissions import IsProjectManager , istaskProjectManager, isTeamMember,isProjectManagerprojectteam
# Create your views here.

class ProjectCreateView(generics.CreateAPIView):
    """
    View for creating a new project.
    """
    serializer_class = ProjectCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the project manager to the current user
        serializer.save(project_manager=self.request.user)


class ProjectListView(generics.ListAPIView):
    """
    View for listing projects for authenticated users that are part or managers of a project.
    """
    serializer_class = ProjectListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Overwriting the queryset to use the Q operator that acts as the logical or 
        to check if the user is in the models.teammembers or is the models.project_manager
        so filters and returns only the iinstances that passes the checks
        """
        user = self.request.user

        # Get the projects where the user is a team member or project manager
        queryset = Project.objects.filter(
            models.Q(project_manager=user) | models.Q(team_members__user=user)
        ).distinct()

        return queryset
    
class ProjectDetailView(generics.RetrieveAPIView):
    """
    View for retrieving a project where the user is either a team member or a project manager.
    """
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Project.objects.filter(
            models.Q(project_manager=user) | models.Q(team_members__user=user)
        ).distinct()
        return queryset

class ProjectUpdateView(generics.UpdateAPIView):
    """
    View for updating a project and is only done by the project manager.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectUpdateSerializer
    permission_classes = [IsProjectManager]
    

class ProjectTeamCreateView(generics.CreateAPIView):
    """
    View for creating a project team member.
    Only the project manager can create team members.
    """
    queryset = ProjectTeamMember.objects.all()
    serializer_class = ProjectTeamCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_project(self):
        project_id = self.kwargs['pk']
        project = get_object_or_404(Project, id=project_id)
        return project
    

    
    
    def perform_create(self, serializer):
        project = self.get_project()
        request_user = self.request.user

        # Check if the request user is the project manager
        if project.project_manager != request_user:
            raise serializers.ValidationError("Only the project manager can add team members.")

            # Get the user being added to the team
        user = serializer.validated_data['user']

    # Check if the user is already a part of the project's team members
        if project.team_members.filter(user=user).exists():
            raise serializers.ValidationError("User is already a part of the project's team members.")
       
        if project.project_manager == user:
            raise serializers.ValidationError("You can't assign task to the Project Manager.")
                
        # Save the team member instance first
        team_member = serializer.save()

        # Then add the project to the team member's projects
        
        

        team_member.projects.add(project)


        return team_member

class ProjectTeamMemberListView(generics.ListAPIView):
    """
    For listing the views for members of a team
    """
    serializer_class = ProjectTeamMemberListSerializer
    permission_classes = [permissions.IsAuthenticated,isTeamMember]
    
    def get_queryset(self):
       user  = self.request.user
       return ProjectTeamMember.objects.filter(projects__team_members__user=user)
    
    

class ProjectTeamRemoveView(generics.DestroyAPIView):
    serializer_class = ProjectTeamRemoveSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectManager]

    def get_queryset(self):
        # Retrieve the project based on the project ID in the URL
        project_id = self.kwargs['project_id']
        return Project.objects.filter(id=project_id)

    def perform_destroy(self, instance):
        # Remove the team member from the project
        team_member_id = self.kwargs['team_member_id']
        instance.team_members.remove(team_member_id)
        
class ProjectTeamAddView(generics.CreateAPIView):
    """
    View for adding a team member to a project.
    """
    serializer_class = ProjectTeamAddSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_project(self):
        # Retrieve the project based on the project ID in the URL
        project_id = self.kwargs['project_id']
        return Project.objects.get(id=project_id)

    def get_serializer_context(self):
        # Add the project and request user to the serializer's context
        context = super().get_serializer_context()
        context['project'] = self.get_project()
        return context
    


class TaskCreateView(generics.CreateAPIView):
    """
    Create task , only project managers can create and can be assigned to only team members
    """
    serializer_class = TaskCreateSerializer
    permission_classes = [permissions.IsAuthenticated,istaskProjectManager]
    
    def get_queryset(self):
        # Filter the queryset to include only the tasks assigned to the projects where the user is the project manager
        user = self.request.user
        return Task.objects.filter(project__project_manager=user) 
    
    def get_project(self):
        # Retrieve the project based on the project ID in the URL
        project_id = self.kwargs['project_id']
        return Project.objects.get(id=project_id)
    
    def get_serializer_context(self):
        # Add the project and request user to the serializer's context
        context = super().get_serializer_context()
        context['project'] = self.get_project()
        return context
    
    

class TaskListView(generics.ListAPIView):
    """_summary_
        View for listing Task and filter for task related to a project
    """
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticated,IsProjectManager]

    def get_queryset(self):
        """This takes the projects id and filter tasks for particular project"""
        project_id = self.kwargs['project_id']
        return Task.objects.filter(project_id=project_id)
    
class TaskUserListView(APIView):
    """Using just custom API VIEW TO WRITE THE VIEWS """
    permissions = [permissions.IsAuthenticated]
    def get(self, request):
        # Get the ProjectTeamMember instance of the currently authenticated user, used first because of the many to one relationship
        project_team_member = self.request.user.projectteammember.first()
        
        # Get the ProjectTeamMember instance of the currently authenticated user
        tasks = Task.objects.filter(assigned_to=project_team_member)
        
        #serialize  and return the json response
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
class TaskUpdateView(generics.UpdateAPIView):
    """
    View for updating the status of a task, only the user assigned to the task
    can update, hence fetches the current user and filters the tasks to only that
    assigned to him.
    """
    serializer_class = TaskUpdateSerializer
    permission_classes =[permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter the queryset to only include tasks assigned to the current team member
        current_user = self.request.user
        return Task.objects.filter(assigned_to__user=current_user)
    
class TaskDeleteView(generics.DestroyAPIView):   
    """This is to delete the task that matches the id , in the lookup field"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, istaskProjectManager]
    #lookup field being id so delete according the id in the task instance and url
    lookup_field = 'id'  # Update the lookup_field attribute
    
    #only work on all filter objects which the user is projectmanager
    def get_queryset(self):
        project_manager = self.request.user
        return Task.objects.filter(project__project_manager=project_manager)
    
    def get_project(self):
        # Retrieve the project based on the project ID in the URL
        project_id = self.kwargs['project_id']
        return Project.objects.get(id=project_id)
    
    
    def perform_destroy(self, instance):
        # Delete the task instance
        instance.delete()
  
    
class ProjectMilestoneCreateView(generics.CreateAPIView):
    """
    View for creating a project milestone.
    Only project managers can create milestones.
    """
    serializer_class = ProjectMilestoneSerializer
    permission_classes = [permissions.IsAuthenticated, istaskProjectManager]

    def perform_create(self, serializer):
        """over writing to save to database after validation"""
        project_id = self.kwargs['project_id']
        project = get_object_or_404(Project, id=project_id)

        # Check if the user is the project manager
        if project.project_manager != self.request.user:
            raise serializers.ValidationError("Only the project manager can create milestones.")

        # Set the project on the milestone before saving
        serializer.save(project=project)


class ProjectMilestoneUpdateView(generics.UpdateAPIView):
    """
    View for updating a milestone.
    Only project managers can update milestones.
    """
    serializer_class = ProjectMilestoneSerializer
    permission_classes = [permissions.IsAuthenticated, istaskProjectManager]
    
    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Milestone.objects.filter(project_id=project_id)

class ProjectMilestoneListView(generics.ListAPIView):
    """
    View for listing project milestones.
    Project managers and project members can view the milestones.
    """
    serializer_class = ProjectMilestoneSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        project = get_object_or_404(Project, id=project_id)

        # Check if the user is the project manager or a project member
        if project.project_manager == self.request.user:
            # User is the project manager, return all milestones for the project
            return Milestone.objects.filter(project=project)
        elif project.team_members.filter(user=self.request.user).exists():
            # User is a project member, return milestones assigned to them
            return Milestone.objects.filter(project=project)

        # User does not have permission to view milestones
        raise PermissionDenied("You do not have permission to view milestones.")



class ProjectMilestoneDetailView(generics.RetrieveAPIView):
    """
    View for retrieving a project milestone.
    Only project managers can view the milestone.
    """
    serializer_class = ProjectMilestoneSerializer
    permission_classes = [permissions.IsAuthenticated, istaskProjectManager]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        project = get_object_or_404(Project, id=project_id)

        # Check if the user is the project manager
        if project.project_manager != self.request.user:
            raise PermissionDenied("You do not have permission to view this milestone.")

        return Milestone.objects.filter(project=project)

class ProjectMilestoneDeleteView(generics.DestroyAPIView):
    """
    View for updating a milestone.
    Only project managers can update milestones.
    """
    serializer_class = ProjectMilestoneSerializer
    permission_classes = [permissions.IsAuthenticated, istaskProjectManager]
    
    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Milestone.objects.filter(project_id=project_id)
    
    
class IssueCreateView(generics.CreateAPIView):
    serializer_class = IssueCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def get_serializer_context(self):
        """
        overwrite the context to include the request pass to the serializer
        """
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def perform_create(self, serializer):
        """Inother for the association to be done"""
        #Get the task
        task = serializer.validated_data['task']
        
        # Ensure that the current user is the assigned_to member of the task
        if task.assigned_to.user != self.request.user:
            raise PermissionDenied("You are not allowed to raise an issue for this task.")

        # Get the associated project of the task
        project = task.project

        # Save the issue with the associated project
        serializer.save(project=project)
        

class IssueUpdateView(generics.UpdateAPIView):
    serializer_class = IssueUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
       
        # Filter the queryset to only include issues associated with the tasks assigned to the current user
        current_user = self.request.user
        return Issue.objects.filter(task__assigned_to__user=current_user)



class IssueListView(generics.ListAPIView):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated,IsProjectManager]

    def get_queryset(self):
        # Filter the queryset to only include issues associated with the projects managed by the current user
        current_user = self.request.user
        project_id = self.kwargs.get('project_id')
        return Issue.objects.filter(project_id=project_id)
    
    
class IssueDestroyView(generics.DestroyAPIView):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Filter the queryset to only include issues created by the current user
        current_user = self.request.user
        return Issue.objects.filter(task__assigned_to__user=current_user, created_by=current_user)