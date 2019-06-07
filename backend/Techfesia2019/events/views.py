from django.shortcuts import render
from .models import Event, Volunteer
from .serializers import EventSerializer, VolunteerSerializer
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from registration.permissions import IsStaffUser
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class EventsListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# class EventRegisterView(generics.CreateAPIView):
#     permission_classes = (IsAuthenticated,)
#
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer


class EventModifyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsStaffUser,)

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class VolunteerListView(generics.ListCreateAPIView):
    permission_classes = (IsStaffUser,)

    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


class VolunteerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsStaffUser,)

    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
