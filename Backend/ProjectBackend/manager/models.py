from django.db import models 
from identity.models import User
# Create your models here.


#MODELS TO TAKE CARE OF THE STORING OF THE managers DETAILS
class ProjectManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20) 

#MODELS TO STORE THE PROJECTS DATA
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(blank=False, null=False , default=None)
    end_date = models.DateTimeField(blank=False, null=False,default=None)
    project_manager = models.ForeignKey(ProjectManager, on_delete=models.CASCADE, related_name='project_manager',)
       
    def __str__(self):
        return self.name
    


#MODEL TO TAKE CARE OF THE STORING OF THE TEAMMEMBERS INFO   
class ProjectTeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20) 
    

    
#MODELS FOR STORING INFOR ABOUT THE TASK , infos such as task of the project, the team member assigned to and the details of the task
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='project')
    name = models.CharField(max_length=20)
    description = models.TextField(blank=False, null=True ,default=None)
    assigned_to = models.ForeignKey(ProjectTeamMember,on_delete=models.CASCADE,related_name='assigned_to')
    deadline = models.DateTimeField(null=False,default=None, blank=False)
    choice = (
        ('completed',('completed')),
        ('not completed',('not completed'))
    )
    status =models.CharField(max_length=20,choices=choice, default='not completed') 
    
    def __str__(self):
            return self.name
    
#MODEL TO TAKE CARE OF THE MILESTONE REACHED WITH EVERY PROJECT  SO AS TO UPDATE THE ORGANIZATION
class Milestone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='projectmilestone')
    description = models.TextField()
    date = models.DateField()
    
    def __str__(self):
            return self.description
#MODELS TO TAKE CARE OF THE RISK ASSOCIATED WITH A PROJECT
class Risk(models.Model):
    risk_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Foreign key to Project model
    description = models.TextField()
    likelihood = models.CharField(max_length=100)
    impact = models.CharField(max_length=100)
    # Other risk fields

    def __str__(self):
        return self.description

#MODELS ASSOCIATED WITH THE ISSUES THAT IS ASSCOIATED WITH A PROJECT
class Issue(models.Model):
    issue_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Foreign key to Project model
    description = models.TextField()
    severity = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    # Other issue fields

    def __str__(self):
        return self.description

#MODELS TO TAKE CARE OF THE CHANGE REQUEST OF A PRODUCT
class ChangeRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Foreign key to Project model
    description = models.TextField()
    status = models.CharField(max_length=100)
    date = models.DateField()
    # Other change request fields

    def __str__(self):
        return self.description

#MODELS TO TAKE CARE OF THE RESOURCES OF A PROJECT
class Resource(models.Model):
    resource_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Foreign key to Project model
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    # Other resource fields

    def __str__(self):
        return self.name