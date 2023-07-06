from rest_framework import permissions



class IsProjectManager(permissions.BasePermission):
    """A class that checks if the user making the requesting is the project manager"""
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is the project manager for the requested project
        return obj.project_manager == request.user
    
class istaskProjectManager(permissions.BasePermission):
    """The permsiions for the task object since is related to the project, then project related to the project manager"""
    def has_object_permission(self, request, view, obj):
        # Check if the user is the project manager for the requested project
        return obj.project.project_manager == request.user
    

class isProjectManagerprojectteam(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
            # Check if the user is the project manager for the requested project
        return obj.project.project_manager == request.user
    


class isTeamMember(permissions.BasePermission):
    """CHECK IF A USER IS A TEAM MEMEBER OF THE PROJECT"""
    def has_object_permission(self, request, view, obj):
        # Check if the user is a project team member for the requested project , using revers relationship with the many to many
        return obj.team_members.filter(user=request.user).exists()