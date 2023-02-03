from django.db import models
from users.models import HODProfile, WorkersProfile

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)
    createdBy = models.OneToOneField(HODProfile, on_delete=models.SET_NULL, null=True)


    def __repr__(self):
        return self.name

class WorkersDepartment(models.Model):
    worker = models.ForeignKey(WorkersProfile, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return self.worker



