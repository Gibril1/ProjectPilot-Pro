from django.http import Http404
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import HODProfile, WorkersProfile
from .models import Task, WorkerTask
from .serializers import TaskSerializer, WorkerTaskSerializer
from app.permissions import HODsPermission, UserEditDeletePermission, WorkersPermission


class TaskCreateView(APIView):
    permission_classes = [IsAuthenticated, HODsPermission]
    def get_hod_profile(self, user):
        try:
            return HODProfile.objects.get(user=user)
        except HODProfile.DoesNotExist:
            raise Http404

    def post(self, request):
        hod = self.get_hod_profile(request.user)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(createdBy = hod)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class TaskView(ListAPIView):
    permission_classes = [IsAuthenticated, HODsPermission]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailsView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AssignTaskView(APIView):
    permission_classes = [HODsPermission]
    def get_task(self, id):
        try:
            return Task.objects.get(id=id)
        except:
            raise Http404
    
    def get_hod(self, id):
        try:
            return HODProfile.objects.filter(user=id).first()
        except:
            raise Http404

    def get_worker_profile(self, id):
        try:
            return WorkersProfile.objects.get(user=id)
        except  WorkersProfile.DoesNotExist:
            raise Http404

    def post(self, request, id):
        task = self.get_task(id)
        createdBy = self.get_hod(request.user)
        worker = self.get_worker_profile(request.data['worker'])
        if task.createdBy != createdBy:
            message = 'You have no permission to assign this task'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        worker_task = WorkerTask.objects.create(
            worker = worker,
            task = task,
            createdBy = createdBy
        )
        serializer = WorkerTaskSerializer(worker_task)
        return Response(serializer.data,status=status.HTTP_200_OK)


    
        
        

class AssignTaskDetailsView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = WorkerTask.objects.all()
    serializer_class = WorkerTaskSerializer


class GetUserTasksView(APIView):
    permission_classes = [IsAuthenticated, WorkersPermission]

    def get_worker_profile(self, user):
        try:
            return WorkersProfile.objects.get(user=user)
        except  WorkersProfile.DoesNotExist:
            raise Http404

    def get(self, request):
        worker_profile = self.get_worker_profile(request.user)
        workers_tasks = WorkerTask.objects.filter(worker=worker_profile).all()
        tasks =  [worker_tasks.task for worker_tasks in workers_tasks]
        task_details = Task.objects.filter(id__in=[task.id for task in tasks])
        serializer = TaskSerializer(task_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



