from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from users.models import WorkersProfile
from ..permissions import WorkersPermission
from ..models import Department, WorkersDepartment, WorkerTask, Task
from ..serializers import WorkersDepartmentSerializers, TaskSerializer

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


class GetAssignedTasks(APIView):
    permission_classes = [WorkersPermission, IsAuthenticated]

    def get_worker(self, id):
        try:
            return WorkersProfile.objects.filter(user=id).first()
        except:
            raise Http404
    
    def get(self, request):
        worker = self.get_worker(request.user)
        assigned_tasks = WorkerTask.objects.filter(worker=worker).all()
        tasks = Task.objects.filter(id__in=assigned_tasks)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
        