from rest_framework.permissions import BasePermission,  SAFE_METHODS

class WorkersPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Worker'

class HODsPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'HOD'



