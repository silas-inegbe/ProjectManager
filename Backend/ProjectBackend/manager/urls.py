from django.urls import path
from .views import (ProjectListView, ProjectDetailView, 
                    ProjectCreateView, ProjectUpdateView,
                    ProjectTeamCreateView , ProjectTeamAddView,ProjectTeamRemoveView
                    ,TaskListView,TaskUpdateView, TaskCreateView
                    ,ProjectMilestoneCreateView, IssueCreateView, IssueUpdateView, ProjectMilestoneDeleteView, IssueDestroyView,IssueListView,
                    ProjectMilestoneListView, TaskDeleteView, TaskUserListView,ProjectMilestoneDetailView, ProjectMilestoneUpdateView)

urlpatterns = [
    # For  projects urls , creatinga n updating url, test passed
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    
    # For Team Members urls 
    path('projects/<int:pk>/team/create/', ProjectTeamCreateView.as_view(), name='project-team-create'),
    path('projects/<int:project_id>/team/add/', ProjectTeamAddView.as_view(), name='project-team-add'),
     path('projects/<int:project_id>/team/remove/<int:team_member_id>/', ProjectTeamRemoveView.as_view(), name='project-team-remove'),
    
    # For adding tasks to a project 
    path('projects/<int:project_id>/tasks/create/',TaskCreateView.as_view(), name='task-create'),
    path('projects/<int:project_id>/tasks/', TaskListView.as_view(), name='task-list'),
    path('projects/user/tasks/', TaskUserListView.as_view(), name='task-list'),
    path('projects/<int:project_id>/tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:id>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    #For milestone views
    path('projects/<int:project_id>/milestones/', ProjectMilestoneListView.as_view(), name='milestone-list'),
    path('projects/<int:project_id>/milestones/<int:pk>/', ProjectMilestoneDetailView.as_view(), name='milestone-detail'),
    path('projects/<int:project_id>/milestones/create/', ProjectMilestoneCreateView.as_view(), name='milestone-create'),
    path('projects/<int:project_id>/milestones/<int:pk>/update/', ProjectMilestoneUpdateView.as_view(), name='milestone-update'),
    path('projects/<int:project_id>/milestones/<int:pk>/delete/', ProjectMilestoneDeleteView.as_view(), name='milestone'),
    #For issues views
    path('projects/<int:project_id>/tasks/<int:task_id>/issues/create/', IssueCreateView.as_view(), name='create_issue'),
    path('issues/<int:pk>/update/', IssueUpdateView.as_view(), name='issue-update'),
    path('issues/<int:pk>/delete/', IssueDestroyView.as_view(), name='issue-delete'),
    path('projects/<int:project_id>/issues/', IssueListView.as_view(), name='issues')
]
    


