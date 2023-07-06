from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView 
from rest_framework.response import Response
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer
# Create your views here.
from allauth.account import app_settings as allauth_account_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import complete_signup
from allauth.account.views import ConfirmEmailView
from allauth.account.models import EmailAddress
from allauth.socialaccount import signals
from allauth.socialaccount.adapter import get_adapter as get_social_adapter
from allauth.socialaccount.models import SocialAccount
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import status
from rest_framework.exceptions import MethodNotAllowed, NotFound
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from dj_rest_auth.views import LoginView
from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.models import TokenModel
from dj_rest_auth.registration.serializers import (
    SocialAccountSerializer, SocialConnectSerializer, SocialLoginSerializer,
    VerifyEmailSerializer, ResendEmailVerificationSerializer
)
from dj_rest_auth.utils import jwt_encode
from dj_rest_auth.views import LoginView

from .serializers import CustomLoginSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import permissions, viewsets
# Import other necessary modules and views

# Create your views here.

# Custom Logout view
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'You have been logged out successfully.'})
        except Exception as e:
            return Response({'error': str(e)}, status=400)


sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password1', 'password2'),
)
# Custom user registration view
class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    
    # Add decorator for sensitive post parameters
    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def gets_response_data(self, user):
        # Handle response data based on email verification settings and authentication method
        if allauth_account_settings.EMAIL_VERIFICATION == allauth_account_settings.EmailVerificationMethod.MANDATORY:
            return {'detail': _('Verification e-mail sent.')}
        
        if api_settings.USE_JWT:
            data = {
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'date_of_birth': user.date_of_birth,
                    'gender': user.gender ,
                    'phone_number':user.phone_number,
                },
                'access_token': self.access_token,
                'refresh_token': self.refresh_token,
            }
            data["gender"] = user.gender
            print("data:", user.gender)
            return api_settings.JWT_SERIALIZER(data, context=self.get_serializer_context()).data
        elif api_settings.SESSION_LOGIN:
            return None
        else:
            return api_settings.TOKEN_SERIALIZER(user.auth_token, context=self.get_serializer_context()).data

    def create(self, request, *args, **kwargs):
        """
        Handle the creation of a new user.
        """
        print(f"before printing: {request.data}")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("serializer:",serializer.validated_data)
        user = self.perform_create(serializer)
        print("Response before it reaches the data:", user)
        headers = self.get_success_headers(serializer.data)
        data = self.gets_response_data(user)
        print("Response data:", data)

        if data:
            response = Response(
                data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        else:
            response = Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

        return response

    def perform_create(self, serializer):
        """
        Save the user instance and perform additional actions.
        """
        user = serializer.save(self.request)
        print("User saved:", user.__dict__)
        if allauth_account_settings.EMAIL_VERIFICATION != allauth_account_settings.EmailVerificationMethod.MANDATORY:
            if api_settings.USE_JWT:
                self.access_token, self.refresh_token = jwt_encode(user)
            elif not api_settings.SESSION_LOGIN:
                # Session authentication isn't active either, so this has to be
                # token authentication
                api_settings.TOKEN_CREATOR(self.token_model, user, serializer)

        complete_signup(
            self.request._request, user,
            allauth_account_settings.EMAIL_VERIFICATION,
            None,
        )
        print(user.__dict__)
        return user


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    
    
    
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.response import Response

class GoogleLoginCallback(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        # Perform the Google OAuth2 login
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        self.login()
        
        # Get the authenticated user's information
        user = self.serializer.validated_data['user']
        token = self.serializer.validated_data['access_token']
        
        # Retrieve or create the SocialAccount for the user
        social_account, _ = SocialAccount.objects.get_or_create(
            provider='google',
            uid=user.socialaccount_set.filter(provider='google').first().uid
        )
        
        # Update the user's email if it has changed
        social_email = user.socialaccount_set.filter(provider='google').first().extra_data.get('email', '')
        if social_email and social_email != user.email:
            user.email = social_email
            user.save()
        
        # Generate a new token for the user
        token = social_account.socialtoken_set.create(
            app=social_account.app,
            token=token,
            token_secret='',
        )
        
        # Return the response with the token or any additional data you need
        response_data = {
            'token': token.token,
            'user_id': user.id,
            'email': user.email,
            # Include any other relevant user data
        }
        return Response(response_data, status=status.HTTP_200_OK)
