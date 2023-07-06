from django.db import models 
from identity.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.







#MODELS TO STORE THE PROJECTS DATA
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(blank=False, null=False , default=None)
    end_date = models.DateTimeField(blank=False, null=False,default=None)
    project_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_manager',)
     
    def __str__(self):
        return self.name
    

#MODEL TO TAKE CARE OF THE STORING OF THE TEAMMEMBERS INFO   
class ProjectTeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projectteammember')
    phonenumber = models.CharField(max_length=20)
    role = models.TextField(max_length=20)
    projects = models.ManyToManyField(Project, related_name='team_members')
    
    def __str__(self):
        return (self.user.first_name + "" + self.user.last_name)   

#MODELS TO TAKE CARE OF THE STORING OF THE managers DETAILS
class ProjectManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    
   
    
    """_summary_
    """    
@receiver(post_save, sender=Project)
def create_project_manager(sender, instance, created, **kwargs):
    if created and not hasattr(instance.project_manager, 'projectmanager'):
        project_manager = ProjectManager.objects.create(user=instance.project_manager)
        project_manager.save()
        
    def __str__(self):
         return self.user.first_name + ' ' + self.user.last_name
            
           

    
#MODELS FOR STORING INFOR ABOUT THE TASK , infos such as task of the project, the team member assigned to and the details of the task
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='project')
    name = models.CharField(max_length=20)
    assigned_to = models.ForeignKey(ProjectTeamMember,models.CASCADE,related_name='assigned_to')
    description = models.TextField(blank=False, null=True ,default=None)
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
    date = models.DateField(auto_now_add=True)
    
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
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='issues', blank=True, null=True) 
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_reporter',null=True)
    description = models.TextField()
    choice =  (('L',('low')),
            ('M',('meduim')),
            ('H',('high')),
            
            )
    choices = (
        ('not solved',('not solved')),
        ('solved',('solved'))
    )
    severity = models.CharField(choices =choice ,max_length=20, default =None)
    status = models.CharField(choices =choices,max_length=20, default ='not solved')
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