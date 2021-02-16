from rest_framework.permissions import SAFE_METHODS , BasePermission , IsAuthenticated
from .views import *
from users.models import LeaderProfile, Teacher, Student


class TeacherListPermission(permissions.BasePermission):
    message = 'Only leader or teachers can see'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if hasattr(request.user, 'teacher'):
                return True
            return False



class TeacherUpdatePermissionClass(permissions.BasePermission):
    message = 'Only teacher can edit'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


            


class StudentUpdatePermission(permissions.BasePermission):
    message = 'Only student can edit'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user    