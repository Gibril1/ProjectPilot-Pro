from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from users.models import WorkersProfile
from ..permissions import WorkersPermission
from ..models import Department, WorkersDepartment
from ..serializers import WorkersDepartmentSerializers

class JoinDepartmentView(APIView):
    permission_classes = [WorkersPermission]

    def get_department(self, id):
        try:
            return Department.objects.get(id=id)
        except Department.DoesNotExist:
            raise Http404

    def get_worker(self, id):
        try:
            return WorkersProfile.objects.filter(user=id).first()
        except:
            raise Http404

    def get(self, request, id):
        department = self.get_department(id)
        worker = self.get_worker(request.user)
        try:
            workers_department = WorkersDepartment.objects.create(
                department = department,
                worker = worker
            )
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer = WorkersDepartmentSerializers(workers_department)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
        