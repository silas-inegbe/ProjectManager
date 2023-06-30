from .models import Project, ProjectManager ,Issue,Milestone,Task,ProjectTeamMember
from identity.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','email']


class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManager
        fields = ['user']

    def to_representation(self, instance):
        return instance.first_name + ' ' + instance.last_name # Return the project manager's first name
    
    
    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        project = validated_data.get('project')
        
        current_user = self.context['request'].user

        # Check if a project manager with the same name exists
        try:
            project_manager = ProjectManager.objects.get(user__first_name__iexact=user_data['first_name'], user__last_name__iexact=user_data['last_name'])

            # Update the existing project manager's details
           
            project_manager.user.save()

            return project_manager
        except ProjectManager.DoesNotExist:
            # Create a new project manager
            
            project_manager = ProjectManager.objects.create(user=current_user, project=project)
            return project_manager


class ProjectTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:    
        model = ProjectTeamMember
        fields = ['id','name','role','phone_number']
        
class ProjectTeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTeamMember
        fields = ['user', 'phonenumber', 'role']

    def create(self, validated_data): 
        """
        The create method takes on the serializer instances and the validated data
        actually takes cares of saving to the database
        """
        #BECAUSE THE PROJECT AND THE REQUEST HAS BEEN PASSED TO THE SERIALIZERS CONTEXT THROUGH THE VIEWS, SO THE CONTEXT INSTANCE OF THE SERIALIZER HAS ACCESS
        # USE SO ASS TO HAVE INFO TO MAKE DECISIONS
        project = self.context['project']
        request_user = self.context['request'].user

        # Check if the request user is the project manager
        if project.project_manager.user != request_user:
            raise serializers.ValidationError("Only the project manager can add team members.")

        # Create the project team member
        project_team_member = ProjectTeamMember.objects.create(
            projects=project,
            **validated_data
        )
        return project_team_member

    def update(self, instance, validated_data):
        project = instance.projects
        request_user = self.context['request'].user

        # Check if the request user is the project manager
        if project.project_manager.user != request_user:
            raise serializers.ValidationError("Only the project manager can update team members.")

        # Update the project team member
        instance.user = validated_data.get('user', instance.user)
        instance.phonenumber = validated_data.get('phonenumber', instance.phonenumber)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance
    

class ProjectTeamMemberListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
   
    class Meta:
        model = ProjectTeamMember
        fields = ['id', 'user', 'phonenumber', 'role', 'projects']  
        


    
class ProjectTeamRemoveSerializer(serializers.Serializer):
    team_member_id = serializers.IntegerField()
   

    def validate_team_member_id(self, value):
        try:
            team_member = ProjectTeamMember.objects.get(id=value)
        except ProjectTeamMember.DoesNotExist:
            raise serializers.ValidationError("Invalid team member ID.")

        # Check if the team member you are removing is part of the project
        project = self.context['project']
        if not project.team_members.filter(id=value).exists():
            raise serializers.ValidationError("Team member is not part of the project.")

        return team_member    

class ProjectTeamAddSerializer(serializers.Serializer):
    phonenumber = serializers.CharField(max_length=20)
    role = serializers.CharField(max_length=20)

    class Meta:
        model = ProjectTeamMember
        fields = ['phonenumber', 'role']

    def create(self, validated_data):
        """
    This method is responsible for creating a new instance of the model
    based on the validated data provided.

    Args:
        validated_data (dict): The validated data from the serializer.

    Returns:
        instance: The created instance of the model.
    """
        
        project = self.context['project']
        user_id = self.context['request'].user.id

        # Create the project team member
        project_team_member = ProjectTeamMember.objects.create(
            user_id=user_id,
            projects=project,
            **validated_data
        )
        return project_team_member
    
   
def validate_team_member_id(self, value):
    try:
        team_member = User.objects.get(id=value)
    except User.DoesNotExist:
        raise serializers.ValidationError("Invalid user ID.")

    # Check if the user is already part of the project
    project = self.context['project']
    if project.team_members.filter(user_id=value).exists():
        raise serializers.ValidationError("User is already part of the project.")

    return team_member
       
    
class ProjectListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing Project instances.
    """
    class Meta:
        model = Project
        fields = ['id', 'name']  # Include the fields you want to display in the project list


class ProjectDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for detailing view new Project instances.
    team_members here because it's a many-to-many field.
    """
    team_members = serializers.SerializerMethodField(read_only=True)
    project_manager = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name','start_date','end_date', 'project_manager','team_members']

    def get_team_members(self, obj):
        # Retrieve the team members of the project
        team_members = obj.team_members.all()

        if team_members.exists():
            # Serialize the team members using the ProjectTeamMemberSerializer
            serializer = ProjectTeamMemberSerializer(team_members, many=True)
            return serializer.data

        # Return an empty list if no team members exist
        return []

    def get_project_manager(self, obj):
        # Retrieve the project manager of the project
        project_manager = obj.project_manager

        if project_manager:
            # Return the first name  and the last name of the project manager and email
            return ([project_manager.first_name + " "+ project_manager.last_name],[project_manager.email])

        # Return None if no project manager exists
        return None


class ProjectCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new Project instances.
    
    """


    class Meta:
        model = Project
        fields = '__all__'  # Include all fields for the detailed view of the project




class ProjectUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating Project instances.
    Includes read-only serialization for team_members.
    """
    
    class Meta:
        model = Project
        fields = ['name', 'end_date',]  # Include the fields that can be updated

    def validate_end_date(self, value):
        """
        Custom validation for the end_date field during project update.
        Only validation now is to check that the start date must be greater than the end_date.
        """
        # Example validation: Ensure the end_date is greater than the start_date
        start_date = self.instance.start_date  # Access the current start_date value
        if value <= start_date:
            raise serializers.ValidationError("End date must be greater than the start date.")
        return value
    
    

class TaskCreateSerializer(serializers.ModelSerializer):
    """" DOES THE VALIDATION AND CREATION OF THE TASK INSTANCE 

    Args:
        serializers (_type_): _description_

    Raises:
        serializers.ValidationError: ERROR IF NOT ASSIGNED TO A MEMBER OF THE PROJECT

    Returns:
        _type_: _description_
    """
    class Meta:
        model = Task
        fields = ['project', 'name', 'assigned_to', 'description', 'deadline']
        read_only_fields = ['status']

    def validate_assigned_to(self, value):
        # Get the project associated with the task
        project = self.context['project']

        # Check if the assigned_to member is part of the project team
        if not project.team_members.filter(id=value.id).exists():
            raise serializers.ValidationError("Assigned to member is not part of the project team.")

        return value 
    
class TaskUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating the status of a task.
    """
    class Meta:
        model = Task
        fields = ['status']

    def validate_status(self, value):
        # Only the assigned_to member can update the status of the task
        request_user = self.context['request'].user

        # Check if the request user is the assigned_to member of the task
        if request_user != self.instance.assigned_to.user:
            raise serializers.ValidationError("Only the assigned_to member can update the status of the task.")
        return value
    
    def update(self, instance, validated_data):
        # Update the task status
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance 
    
class TaskListSerializer(serializers.ModelSerializer):
    """
    Serializer for the task list, accessible only to the project manager.
    """

    project = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'project', 'name', 'assigned_to', 'description', 'deadline', 'status']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # Check if the request user is the project manager
        request_user = self.context['request'].user
        project_manager = instance.project.project_manager.user
        if request_user != project_manager:
            raise serializers.ValidationError("Only the project manager can access the task list.")
        
        return data

