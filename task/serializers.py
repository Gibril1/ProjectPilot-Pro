from rest_framework import serializers
from .models import WorkersDepartment, Task, WorkerTask



class WorkersDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkersDepartment
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class WorkerTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerTask
        fields = '__all__'