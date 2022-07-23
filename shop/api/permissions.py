from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to teacher users.
    """
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_staff)
