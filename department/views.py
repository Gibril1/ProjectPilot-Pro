from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer
from .serializers import DepartmentSerializers, WorkersDepartmentSerializers
from app.permissions import HODsPermission, WorkersPermission,UserEditDeletePermission
from .models import Department, WorkersDepartment


# creating a new department
class DepartmentView(APIView):
    permission_classes = [IsAuthenticated, HODsPermission]

    def post(self, request):
        serializer = DepartmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(hod=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# list all the departments
class ListDepartmentsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


# update and delete departments
class DepartmentDetailsView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


# join a department
class JoinDepartmentView(APIView):
    permission_classes = [WorkersPermission]
    def get_department(self, id):
        try:
            return Department.objects.get(id=id)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, id):
        department = self.get_department(id) 
        try:
            workers_department = WorkersDepartment.objects.create(
                department = department,
                worker = request.user
            )
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer = WorkersDepartmentSerializers(workers_department)
        return Response(serializer.data, status=status.HTTP_200_OK)


# lists the members of a department
class GetMembersOfDepartment(APIView):
    permission_classes = [IsAuthenticated, HODsPermission]
    def get_department(self, id):
        try:
            return Department.objects.get(id=id)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, id):
        department = self.get_department(id)
        departments = WorkersDepartment.objects.filter(department=department).all()
        workers = [workers_department.worker for workers_department in list(departments)]
        workers_profile = User.objects.filter(id__in=[worker.id for worker in workers])
        serializer = UserSerializer(workers_profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# get all the departments a user has joined
class GetUserDepartmentView(APIView):
    permission_classes=[WorkersPermission, IsAuthenticated]
    def get(self, request):
        workers_departments = WorkersDepartment.objects.filter(worker=request.user).all()
        departments = [worker_departments.department for worker_departments in workers_departments]
        department_details = Department.objects.filter(id__in=[department.id for department in departments])
        serializer = DepartmentSerializers(department_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


        


