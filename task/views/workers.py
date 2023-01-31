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

    def get(self, request, id):
        department = self.get_department(id)
        worker = WorkersProfile.objects.filter(user=request.user).first()
        if not worker:
            message = f'Worker with id of { request.user } does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        try:
            workers_department = WorkersDepartment.objects.create(
                department = department,
                worker = worker
            )
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer = WorkersDepartmentSerializers(workers_department)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
        