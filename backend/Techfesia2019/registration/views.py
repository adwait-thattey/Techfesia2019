from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.six import text_type
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework import exceptions as rest_exceptions

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

class FirebaseAuthenticationView(APIView):
    """
    Takes email and uid.
    Verifies from firebase.
    If user does not exist, creates user.
    Finally provides token
    """

    def post(self, request):
        email = request.data.get('email')
        uid = request.data.get('uid')
        user_obj = User.objects.filter(email=email).first()

        if not (user_obj and hasattr(user_obj,"firebaseuser")):
            sr = serializers.FirebaseUserSerializer(data=request.data)
            if sr.is_valid():
                firebase_user = sr.save()
                user_obj = firebase_user.user

        firebase_token_pair_serializer =  serializers.FirebaseTokenObtainPairSerializer(data=request.data)

        if firebase_token_pair_serializer.is_valid():
            tokens = serializers.FirebaseTokenObtainPairSerializer.get_token_object(user_obj)
            return Response(status=status.HTTP_200_OK, data=tokens)
        else:
            raise rest_exceptions.AuthenticationFailed()



firebase_token_obtain_pair = FirebaseTokenObtainPairView.as_view()
