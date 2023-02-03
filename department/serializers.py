from rest_framework.serializers import ModelSerializer
from .models import Department


class DepartmentSerializers(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'