from rest_framework import serializers
from .models import Task, WorkerTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class WorkerTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerTask
        fields = '__all__'