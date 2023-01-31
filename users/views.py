from django.shortcuts import render
from django.http import Http404
from .serializers import RegistrationSerializer, HODSerializer, WorkerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission,  SAFE_METHODS, IsAuthenticatedOrReadOnly
from rest_framework import status
from .models import HODProfile, WorkersProfile

# Create your views here.
class WorkersPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Worker'

class HODsPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'HOD'


class UserEditDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HODView(APIView):
    permission_classes = [HODsPermission]
    def post(self, request):
        serializer = HODSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HODDetailsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,UserEditDeletePermission]

    def get_hod(self, id):
        try:
            return HODProfile.objects.filter(user=id).first()
        except HODProfile.DoesNotExist:
            raise Http404

    def put(self, request, id):
        hod = self.get_hod(id)
        serializer = HODSerializer(hod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class WorkerView(APIView):
    permission_classes = [WorkersPermission]
    def post(self, request):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkerDetailsView(APIView):
    permission_classes = [UserEditDeletePermission]

    def get_worker(self, id):
        try:
            return WorkersProfile.objects.filter(user=id).first()
        except WorkersProfile.DoesNotExist:
            raise Http404

    def put(self, request, id):
        worker = self.get_worker(id)
        serializer = WorkerSerializer(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


