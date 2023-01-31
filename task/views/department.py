from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from users.models import HODProfile
from ..serializers import DepartmentSerializers
from ..permissions import HODsPermission, UserEditDeletePermission
from ..models import Department

# Create your views here.
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

class DepartmentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializers(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DepartmentDetailsView(APIView):
    permission_classes = [UserEditDeletePermission]
    def get_department(self,id):
        try:
            return Department.objects.get(id=id)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, id):
        department = self.get_department(id)
        serializer = DepartmentSerializers(department)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        department = self.get_department(id)
        serializer = DepartmentSerializers(department,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id):
        department = self.get_department(id)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

