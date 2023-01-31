from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from users.models import HODProfile
from ..serializers import DepartmentSerializers
from ..permissions import HODsPermission
from ..models import Department

class UserEditDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.hod.user == request.user

class DepartmentView(APIView):
    permission_classes = [IsAuthenticated, HODsPermission]
    def post(self, request):
        hod = HODProfile.objects.filter(user=request.user).first()
        if not hod:
            message = f'HOD with id of {request.user} does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(hod=hod)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers

    
class DepartmentDetailsView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers

