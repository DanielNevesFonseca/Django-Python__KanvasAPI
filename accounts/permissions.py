from rest_framework import permissions
from rest_framework.views import View
from courses.models import Course


class IsSuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.user.is_authenticated and request.user.is_superuser


class IsCourseParticipantPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user in obj.course.students.all()
            or request.user.is_superuser
        )


class IsSuperUserOrReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (
            request.user.is_authenticated
            and request.user.is_superuser
            or request.method in permissions.SAFE_METHODS
        )
