from rest_framework import permissions



class IsProjectManager(permissions.BasePermission):
    """A class that checks if the user making the requesting is the project manager"""
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is the project manager for the requested project
        return obj.project_manager == request.user



def has_object_permission(self, request, view, obj):
        # Check if the user is a project team member for the requested project , using revers relationship with the many to many
        return obj.team_members.filter(user=request.user).exists()