from django.shortcuts import render
from django.http import Http404
from .serializers import RegistrationSerializer, HODSerializer, WorkerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from .models import HODProfile, WorkersProfile
from task.permissions import HODsPermission, WorkersPermission


class UserEditDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

# Create your views here.
class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HODView(CreateAPIView):
    permission_classes = [IsAuthenticated, HODsPermission]
    queryset = HODProfile.objects.all()
    serializer_class = HODSerializer
    


class HODDetailsView(RetrieveUpdateAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = HODProfile.objects.all()
    serializer_class = HODSerializer
    

class WorkerView(CreateAPIView):
    permission_classes = [WorkersPermission]
    queryset = WorkersProfile.objects.all()
    serializer_class = WorkerSerializer

    
class WorkerDetailsView(RetrieveUpdateAPIView, UserEditDeletePermission):
    permission_classes = [UserEditDeletePermission, IsAuthenticated]
    queryset = WorkersProfile.objects.all()
    serializer_class = WorkerSerializer

