from rest_framework import permissions


class IsStaffUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True
        else:
            return False


class IsAuthenticatedOrGet(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method == 'GET'
