from django.db import models
from django.utils import timezone
from users.models import HODProfile, WorkersProfile


class Task(models.Model):
    code = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=1000000)
    progress = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    createdBy = models.ForeignKey(HODProfile, on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True)

class WorkerTask(models.Model):
    worker = models.ForeignKey(WorkersProfile, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(HODProfile, on_delete=models.SET_NULL, null=True)

