from rest_framework import serializers
from .models import Department, WorkersDepartment

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class WorkersDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkersDepartment
        fields = '__all__'