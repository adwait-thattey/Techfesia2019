from .models import Event, Volunteer
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'description', 'rules', 'fees', 'prerequisites', 'faq')
        fields += ('time', 'venue', 'current_participants', 'max_participants', 'volunteer_list')


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ('name', 'task')
