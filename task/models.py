from django.db import models
from users.models import HODProfile

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)
    hod = models.OneToOneField(HODProfile, on_delete=models.SET_NULL, null=True)
