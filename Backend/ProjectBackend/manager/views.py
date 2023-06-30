from django.shortcuts import render
from .models import Project,ProjectTeamMember,ProjectManager ,Task
from rest_framework import generics, permissions
from django.db import models
from .serializers import( ProjectCreateSerializer,ProjectDetailSerializer,ProjectListSerializer,
                         ProjectTeamMember,ProjectUpdateSerializer,TaskListSerializer,TaskCreateSerializer,TaskUpdateSerializer,ProjectTeamRemoveSerializer,ProjectTeamAddSerializer,ProjectTeamCreateSerializer)
from .permissions import IsProjectManager
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
        )

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
        )
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
    permission_classes = [IsProjectManager]
    
    

class ProjectTeamRemoveView(generics.DestroyAPIView):
    serializer_class = ProjectTeamRemoveSerializer
    permission_classes = [permissions.IsAuthenticated,IsProjectManager]

    def get_queryset(self):
        # Retrieve the project based on the project ID in the URL
        project_id = self.kwargs['project_id']
        return Project.objects.filter(id=project_id)

    def get_object(self):
        # Get the project from the queryset
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset)

        # Add the project to the serializer's context
        self.serializer_class.context['project'] = obj

        return obj

    def perform_destroy(self, instance):
        # Remove the team member from the project
        team_member_id = self.request.data.get('team_member_id')
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
    


class TaskListView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [IsProjectManager]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Task.objects.filter(project_id=project_id)
    
class TaskUpdateView(generics.UpdateAPIView):
    """
    View for updating the status of a task.
    """
    serializer_class = TaskUpdateSerializer
    permission_classes =[permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter the queryset to only include tasks assigned to the current team member
        current_user = self.request.user
        return Task.objects.filter(assigned_to__user=current_user)