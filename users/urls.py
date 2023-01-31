from django.urls import path
from .views import (
    RegistrationView, 
    HODView,  
    HODDetailsView,  
    WorkerView,
    WorkerDetailsView
    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistrationView.as_view(), name='register_user'),
    path('register/hod', HODView.as_view(), name='register_hod'),
    path('hod/<int:id>', HODDetailsView.as_view(), name='edit_hod_details'),
    path('register/worker', WorkerView.as_view(), name='register_worker'),
    path('worker/<int:id>', WorkerDetailsView.as_view(), name='edit_worker_details'),
]