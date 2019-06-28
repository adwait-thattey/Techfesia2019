from rest_framework import permissions


class IsStaffUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True
        else:
            return False

    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True
        else:
            return False


class IsStaffUserOrPost(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser or request.method == 'POST':
            return True
        else:
            return False

    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser or request.method == 'POST':
            return True
        else:
            return False


class IsAuthenticatedOrPost(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method == 'POST'