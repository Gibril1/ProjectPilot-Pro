from django.http import Http404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from users.models import HODProfile
from ..models import Task, WorkerTask
from ..serializers import TaskSerializer, WorkerTaskSerializer
from ..permissions import HODsPermission, UserEditDeletePermission



class TaskView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, HODsPermission]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailsView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AssignTask(APIView):
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

    def post(self, request, id):
        task = self.get_task(id)
        createdBy = self.get_hod(request.user)
        serializer = WorkerTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task=task, createdBy = createdBy)

class AssignTaskDetails(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = WorkerTask.objects.all()
    serializer_class = WorkerTaskSerializer
