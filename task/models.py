from django.db import models
from users.models import User
from department.models import Department


class Project(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self) -> str:
        return self.name
    

class Task(models.Model):
    PROGRESS_TYPE = [
        ('In Progress', 'In Progress'),
        ('Unassigned', 'Unassigned'),
        ('Completed', 'Completed'),
        ('In Review', 'In Review')
    ]
    code = models.CharField(max_length=10, null=True) # any four digit code for the task [Optional]
    type = models.CharField(max_length=20, null=True)
    description = models.TextField()
    progress = models.IntegerField(default=0)
    progress_type = models.CharField(max_length=20, choices=PROGRESS_TYPE, default='Unassigned')
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True)


    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# this model holds the tasks assigned to the worker
class WorkerTask(models.Model):
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='worker')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='hod')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


