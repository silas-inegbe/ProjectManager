from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomRegisterView, GoogleLogin

urlpatterns = [
    # Custom registration view
    path('api/auth/registration/', CustomRegisterView.as_view()),

    # Token-based authentication using JWT
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_create'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/google', GoogleLogin.as_view(), name='google_login'),
    # Other URLs and views
    # ...

    # You can include additional URLs and views as needed
    # ...

    # Example using Django Rest Auth (uncomment to enable)
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
