from rest_framework import serializers
from events.models import TeamEvent, SoloEvent
from .models import Team, SoloEventRegistration, TeamEventRegistration, TeamMember


class TeamSerializer(serializers.ModelSerializer):
    members = serializers.SlugRelatedField(many=True, read_only=True, slug_field='get_user_username')
    leader = serializers.SlugRelatedField(read_only=True, slug_field='username')
    invitees = serializers.SlugRelatedField(many=True, read_only=True, slug_field='get_user_username')
    events = serializers.SlugRelatedField(many=True, read_only=True, slug_field='get_event_public_id')

    class Meta:
        model = Team
        fields = ['public_id', 'name', 'leader', 'members', 'invitees', 'events']

    def is_valid(self, raise_exception=False):
        return super().is_valid()


class TeamMemberSerializer(serializers.ModelSerializer):
    leader = serializers.SlugRelatedField(read_only=True, slug_field='get_user_username')
    team = serializers.SlugRelatedField(read_only=True, slug_field='public_id')

    class Meta:
        model = TeamMember
        fields = ['team', 'team_name', 'leader', 'status']


class TeamEventRegistrationSerializer(serializers.ModelSerializer):
    registration_id = serializers.CharField(source='public_id', read_only=True)
    team_id = serializers.SlugRelatedField(source='team', read_only=True, slug_field='public_id')
    
    class Meta:
        model = TeamEventRegistration
        fields = ['registration_id', 'team_id', 'status']


# This Serializer is To List all Registrations for a Team Event
class TeamEventRegistrationsSerializer(serializers.ModelSerializer):
    registrations = TeamEventRegistrationSerializer(source='teameventregistration_set', many=True)

    class Meta:
        model = TeamEvent
        fields = ['public_id', 'event_type', 'registrations']


class SoloEventRegistrationSerializer(serializers.ModelSerializer):
    registration_id = serializers.CharField(source='public_id', read_only=True)
    user_id = serializers.SlugRelatedField(source='profile', read_only=True, slug_field='get_user_username')

    class Meta:
        model = SoloEventRegistration
        fields = ['registration_id', 'user_id', 'status']


# This Serializer is To List all Registrations for a Solo Event
class SoloEventRegistrationsSerializer(serializers.ModelSerializer):
    registrations = SoloEventRegistrationSerializer(source='soloeventregistration_set', many=True)

    class Meta:
        model = SoloEvent
        fields = ['public_id', 'event_type', 'registrations']
