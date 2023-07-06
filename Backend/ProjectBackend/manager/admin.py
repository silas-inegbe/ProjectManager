from django.contrib import admin
from .models import Project , ProjectTeamMember, Task , Issue, Milestone, ProjectManager , ProjectTeamMember
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models
# Register your models here.
@admin.register(Project)
#FOR REGISTERING OF THE PROJECTS TO THE ADMIN
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project_manager']
    # Customize other options as needed
    
@admin.register(Task)
#FOR REGISTERING OF THE TASKS TO THE ADMIN
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project', 'assigned_to']
    # Customize other options as needed
    
@admin.register(Milestone)
#FOR REGISTERING OF THE MILESTONE TO THE ADMIN
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project', 'description']
    # Customize other options as needed    

@admin.register(ProjectTeamMember)
class ProjectTeammemberAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple(verbose_name='Projects', is_stacked=False)},
    }
    
    list_display = ['user','role','phonenumber']
@admin.register(Issue)
#FOR REGISTERING OF THE MILESTONE TO THE ADMIN
class IssueAdmin(admin.ModelAdmin):
    list_display = ['issue_id', 'task', 'description','severity','status']
    # Customize other options as needed 
    
   
