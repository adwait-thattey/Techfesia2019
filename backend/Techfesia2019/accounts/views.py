from django.shortcuts import get_object_or_404

# Create your views here.
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from registration.decorators import is_user_calling_self
from registration.models import User


class EmailConfirmed(APIView):
    """
        Deals with email confirmation of a user
    """

    permission_classes = (IsAuthenticated,)

    @method_decorator(is_user_calling_self)
    def get(self, request, username):
        """
            return True if email
        """

        user = get_object_or_404(User, username=username)
        #
        # # TODO Replace these lines with a common auth wrapper or permission class
        # if not request.user.is_staff:
        #     if request.user != user:
        #         return Response(status=status.HTTP_403_FORBIDDEN,
        #                         data={"message": "You do not have permission to perform this action"})

        return Response(status=status.HTTP_200_OK, data={"email_confirmed": user.email_confirmed})
