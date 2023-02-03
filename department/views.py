from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from users.models import HODProfile, WorkersProfile
from .serializers import DepartmentSerializers, WorkersDepartmentSerializers
from app.permissions import HODsPermission, WorkersPermission,UserEditDeletePermission
from .models import Department, WorkersDepartment



class DepartmentView(APIView):
    permission_classes = [IsAuthenticated, HODsPermission]
    def get_hod(self, id):
        try:
            return HODProfile.objects.filter(user=id).first()
        except:
            raise Http404

    def post(self, request):
        hod = self.get_hod(request.user)
        serializer = DepartmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(hod=hod)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentsView(ListAPIView):
    permission_classes = [IsAuthenticated, HODsPermission]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers

    
class DepartmentDetailsView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class JoinDepartmentView(APIView):
    permission_classes = [WorkersPermission]

    def get_department(self, id):
        try:
            return Department.objects.get(id=id)
        except Department.DoesNotExist:
            raise Http404

    def get_worker(self, id):
        try:
            return WorkersProfile.objects.filter(user=id).first()
        except:
            raise Http404

    def get(self, request, id):
        department = self.get_department(id)
        worker = self.get_worker(request.user)
        try:
            workers_department = WorkersDepartment.objects.create(
                department = department,
                worker = worker
            )
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer = WorkersDepartmentSerializers(workers_department)
        return Response(serializer.data, status=status.HTTP_200_OK)


