from django.urls import path
from .views import (ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView,ProjectTeamCreateView)

urlpatterns = [
    # For all projects
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    
    # For Team Members urls
     path('projects/<int:project_id>/team/create/', ProjectTeamCreateView.as_view(), name='project-team-create'),
]

