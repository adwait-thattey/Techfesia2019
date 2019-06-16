from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class Hello(APIView):
    """
        Get request is open. Post is protected
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):

        return Response(status=status.HTTP_200_OK, data={"message":"GET Hello"})

    def post(self, request):

        return Response(status=status.HTTP_200_OK, data={"message":"POST Hello"})