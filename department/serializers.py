from rest_framework.serializers import ModelSerializer
from .models import Department, WorkersDepartment


class DepartmentSerializers(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class WorkersDepartmentSerializers(ModelSerializer):
    class Meta:
        model = WorkersDepartment
        fields = '__all__'