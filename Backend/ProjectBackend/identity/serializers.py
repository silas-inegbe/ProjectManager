

from django.core.exceptions import ValidationError as DjangoValidationError
from allauth.account.adapter import get_adapter
from django.utils.translation import gettext_lazy as __
from rest_framework import serializers
from allauth.account.utils import setup_user_email
# OVERWRITING THE CUSTOMSIGNUPVIEW
from dj_rest_auth.registration.serializers import RegisterSerializer 
from django.contrib.auth import get_user_model
from allauth.account import app_settings as allauth_account_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.base import AuthProcess
from allauth.utils import email_address_exists, get_username_max_length
from dj_rest_auth.serializers import LoginSerializer




#CUSTOM REGISTER SERIALIZER 
class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=True)
    phone_number = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=(('Male', 'Male'),('Female', 'Female')),required=True)
    username = None
 # which is called after a user has successfully signed up, provides hook to perfoem additional function   
    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.date_of_birth = self.validated_data.get('date_of_birth', '')
        user.gender = self.validated_data.get('gender', '')
        user.phone_number = self.validated_data.get('phone_number', '')
        
        user.save()
        print(f"at serialised data: {user}")

# It retrieves the cleaned (validated and sanitized) data from the form or serializer instance
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'date_of_birth':self.validated_data.get('date_of_birth', ''),
            'gender':self.validated_data.get('gender', ''),
            'phone_number':self.validated_data.get('phone_number','')
        }
            
    def validate_username(self, username):
        pass



class CustomLoginSerializer(LoginSerializer):
    username = None; 
    
    def _validate_username(self, username,password):    
        pass;