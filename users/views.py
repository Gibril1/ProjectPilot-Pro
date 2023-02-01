from .serializers import RegistrationSerializer, HODSerializer, WorkerSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from .models import HODProfile, WorkersProfile, User
from task.permissions import HODsPermission, WorkersPermission


class UserEditDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class HODView(CreateAPIView):
    permission_classes = [IsAuthenticated, HODsPermission]
    queryset = HODProfile.objects.all()
    serializer_class = HODSerializer
    


class HODDetailsView(RetrieveUpdateAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = HODProfile.objects.all()
    serializer_class = HODSerializer
    

class WorkerView(CreateAPIView):
    permission_classes = [IsAuthenticated, WorkersPermission]
    queryset = WorkersProfile.objects.all()
    serializer_class = WorkerSerializer

    
class WorkerDetailsView(RetrieveUpdateAPIView, UserEditDeletePermission):
    permission_classes = [UserEditDeletePermission, IsAuthenticated]
    queryset = WorkersProfile.objects.all()
    serializer_class = WorkerSerializer

