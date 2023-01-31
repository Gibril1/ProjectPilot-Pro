from django.urls import path
from .views import RegistrationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegistrationView.as_view(), name='register_user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]