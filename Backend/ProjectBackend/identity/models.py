from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings

# This the user manager responsible for interacting with the database such as creating accounts to the database
class UserManager(BaseUserManager):
    def create_user(self, email,password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        # creates or istantiantes a new object of the model class of the manager
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255 ,blank=True, null=True)
    last_name = models.CharField(max_length=255,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
   
    choices = [
            ("M","Male"),
            ("FM","Female"),
            ]
    gender = models.CharField(choices= choices ,max_length=50, blank=True, null=True) 
    date_of_birth = models.DateField(blank=True, null=True) 
    phone_number = models.CharField(max_length=20 ,default=None , null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def name_field(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name_field() 
    
    