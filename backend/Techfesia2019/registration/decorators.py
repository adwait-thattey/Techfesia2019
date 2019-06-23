from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from registration.models import User


def is_user_calling_self(func):
    """
    Allows the request to pass if the user is a staff of if the user is requesting
    the object for herself.
    Else returns 403
    """

    def checker(request, *args, **kwargs):
        username = kwargs['username']
        user = get_object_or_404(User, username=username)
        if not request.user.is_staff:
            if request.user != user:
                return Response(status=status.HTTP_403_FORBIDDEN,
                                data={"message": "You do not have permission to perform this action"})

        return func(request, *args, **kwargs)

    return checker


def email_confirmation_required(func):
    """
    A decorator which allows to access route only if email for current user has been confirmed.
    THE DECORATOR login_required MUST ALWAYS PRECEDE THIS.
    i.e. ensure that user is logged on before this decorator is called
    """

    def checker(request, *args, **kwargs):
        if request.user.emailconfirmation.email_confirmed is True:
            return func(request, *args, **kwargs)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data={
                "error": "Please confirm your email",
                "message": "You can not perform this action until your email is confirmed. In case you didnt receive \
                           the confirmation email, you can ping the below route to send another email ",
                "route": ""
            })
        # TODO: Add the confirmation route above

    return checker
