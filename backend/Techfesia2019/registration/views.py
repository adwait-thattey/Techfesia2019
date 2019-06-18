from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.views import TokenViewBase

from registration import serializers
from registration.models import User


class Hello(APIView):
    """
        Get request is open. Post is protected
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        return Response(status=status.HTTP_200_OK, data={"message": "GET Hello"})

    def post(self, request):
        return Response(status=status.HTTP_200_OK, data={"message": "POST Hello"})



class FirebaseTokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = serializers.FirebaseTokenObtainPairSerializer


firebase_token_obtain_pair = FirebaseTokenObtainPairView.as_view()