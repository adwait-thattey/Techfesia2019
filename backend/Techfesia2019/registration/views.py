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


class FirebaseAuthenticationView(APIView):
    """
    Takes email and uid.
    Verifies from firebase.
    If user does not exist, creates user.
    Finally provides token
    """

    def post(self, request):
        email = request.data.get('email')

        user_obj = User.objects.filter(email=email).first()

        if not (user_obj and user_obj.firebaseuser):
            sr = serializers.FirebaseUserSerializer(data=request.data)
            if sr.is_valid():
                sr.save()

        token_sr = serializers.FirebaseTokenObtainPairSerializer(data=request.data)

        if token_sr.is_valid():
            return Response(status=status.HTTP_200_OK, data=token_sr.data)


class FirebaseTokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = serializers.FirebaseTokenObtainPairSerializer


firebase_token_obtain_pair = FirebaseTokenObtainPairView.as_view()
