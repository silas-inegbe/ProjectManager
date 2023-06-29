from django.shortcuts import render
from .models import Project,ProjectTeamMember,ProjectManager
from rest_framework import generics, permissions
from django.db import models
from .serializers import( ProjectCreateSerializer,ProjectDetailSerializer,ProjectListSerializer,
                         ProjectTeamMember,ProjectUpdateSerializer,ProjectTeamCreateSerializer)
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