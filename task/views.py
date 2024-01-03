from django.http import Http404
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from department.models import Department
from .models import Task, WorkerTask, Project
from .serializers import TaskSerializer, WorkerTaskSerializer, ProjectSerializer
from app.permissions import HODsPermission, UserEditDeletePermission, WorkersPermission

# create a project
class ProjectCreateView(APIView):
    permission_classes = [IsAuthenticated, HODsPermission | IsAdminUser]

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailsView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# get projects in a department
class GetDepartmentProjects(APIView):
    permission_classes = [IsAdminUser | HODsPermission, IsAuthenticated]

    def get_department_by_id(self, id):
        try:
            return Department.objects.get(id=id)
        except Department.DoesNotExist:
            raise Http404
        
    def get(self, request, id):
        department = self.get_department_by_id(id)
        projects = Project.objects.filter(department=department).all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# create a task
class TaskCreateView(APIView):
    permission_classes = [IsAuthenticated, HODsPermission]
    def post(self, request): 
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskDetailsView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [IsAuthenticated, UserEditDeletePermission]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



# TODO

'''
get all the tasks in a department
    
get all completed tasks
    
get all in progress tasks
    
get unassigned tasks
    
get tasks due a particular date and time
'''
 

class AssignTaskView(APIView):
    permission_classes = [HODsPermission]
    def get_task(self, id):
        try:
            return Task.objects.get(id=id)
        except:
            raise Http404
    
    def get_worker_profile(self, id):
        try:
            user = User.object.get(id=id)
            if user.role == 'Worker':
                return user
            return None
        except:
            raise Http404

    def post(self, request, id):
        task = self.get_task(id)
        worker = self.get_worker_profile(request.data['worker'])
        if not worker:
            message = 'This user is not a worker'
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)
        if task.created_by != request.user:
            message = 'You have no permission to assign this task'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        worker_task = WorkerTask.objects.create(
            worker = worker,
            task = task,
            created_by = request.user
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
            return User.objects.get(user=user)
        except  User.DoesNotExist:
            raise Http404

    def get(self, request):
        worker_profile = self.get_worker_profile(request.user)
        workers_tasks = WorkerTask.objects.filter(worker=worker_profile).all()
        tasks =  [worker_tasks.task for worker_tasks in workers_tasks]
        task_details = Task.objects.filter(id__in=[task.id for task in tasks])
        serializer = TaskSerializer(task_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



