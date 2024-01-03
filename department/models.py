from django.db import models
from users.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __repr__(self):
        return self.name

class WorkersDepartment(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return self.worker



