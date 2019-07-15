from rest_framework import permissions

def SelfOrStaff(permissions.BasePermission):
    """
    Allow user access only if it is requesting his own data
    or if the user is staff.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        elif request.user == obj:
            return True
        else:
            return False