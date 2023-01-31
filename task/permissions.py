from rest_framework.permissions import BasePermission,  SAFE_METHODS

class WorkersPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Worker'

class HODsPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'HOD'


class UserEditDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
