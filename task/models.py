from django.db import models
from users.models import HODProfile, WorkersProfile
from department.models import Department

# Create your models here.

class WorkersDepartment(models.Model):
    worker = models.ForeignKey(WorkersProfile, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Task(models.Model):
    code = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=20, null=True)
    dscription = models.CharField(max_length=20)
    progress = models.IntegerField()
    done = models.BooleanField()
    createdBy = models.ForeignKey(HODProfile, on_delete=models.CASCADE)

class WorkerTask(models.Model):
    worker = models.ForeignKey(WorkersProfile, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(HODProfile, on_delete=models.SET_NULL, null=True)

