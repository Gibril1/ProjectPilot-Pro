from django.db import models
from users.models import HODProfile, WorkersProfile






class Task(models.Model):
    code = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=20)
    progress = models.IntegerField()
    done = models.BooleanField()
    createdBy = models.ForeignKey(HODProfile, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_created=True)
    due_date = models.DateField(null=True)

class WorkerTask(models.Model):
    worker = models.ForeignKey(WorkersProfile, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(HODProfile, on_delete=models.SET_NULL, null=True)

