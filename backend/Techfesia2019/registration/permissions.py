from rest_framework import permissions


class IsStaffUserOrPost(permissions.BasePermission):

    def has_permission(self, request, view):
        # print(request.user, request.user.is_authenticated, request.user.is_staff)
        if request.user.is_authenticated and request.user.is_staff:
            return True
        elif request.method == 'POST':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # print(request.user, request.user.is_authenticated, request.user.is_staff)
        if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
            return True
        elif request.method == 'POST':
            return True
        else:
            return False


class IsStaffUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
            return True
        else:
            return False


class IsStaffUserOrAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated or request.user.is_staff or request.user.is_superuser:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated or request.user.is_staff or request.user.is_superuser:
            return True
        else:
            return False
