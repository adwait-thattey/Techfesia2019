from rest_framework import serializers
from events.models import TeamEvent, SoloEvent
from .models import Team, SoloEventRegistration, TeamEventRegistration, TeamMember


class TeamSerializer(serializers.ModelSerializer):
    teamId = serializers.CharField(source='public_id', read_only=True)
    members = serializers.SlugRelatedField(many=True, read_only=True, slug_field='get_user_username')
    leader = serializers.SlugRelatedField(read_only=True, slug_field='username')
    invitees = serializers.SlugRelatedField(many=True, read_only=True, slug_field='get_user_username')
    events = serializers.SlugRelatedField(many=True, read_only=True, slug_field='get_event_public_id')

    class Meta:
        model = Team
        fields = ['teamId', 'name', 'leader', 'members', 'invitees', 'events']

    def is_valid(self, raise_exception=False):
        return super().is_valid()


class TeamMemberSerializer(serializers.ModelSerializer):
    leader = serializers.SlugRelatedField(read_only=True, slug_field='get_user_username')
    name = serializers.CharField(source='team_name', read_only=True)
    teamId = serializers.SlugRelatedField(source='team', read_only=True, slug_field='public_id')

    class Meta:
        model = TeamMember
        fields = ['teamId', 'name', 'leader', 'status']


class TeamEventRegistrationSerializer(serializers.ModelSerializer):
    registrationId = serializers.CharField(source='public_id', read_only=True)
    teamId = serializers.SlugRelatedField(source='team', read_only=True, slug_field='public_id')
    
    class Meta:
        model = TeamEventRegistration
        fields = ['registrationId', 'teamId', 'status']


# This Serializer is To List all Registrations for a Team Event
class TeamEventRegistrationsSerializer(serializers.ModelSerializer):
    eventPublicId = serializers.CharField(source='public_id', read_only=True)
    eventType = serializers.CharField(source='event_type', read_only=True)
    registrations = TeamEventRegistrationSerializer(source='teameventregistration_set', many=True)

    class Meta:
        model = TeamEvent
        fields = ['eventPublicId', 'eventType', 'registrations']


class SoloEventRegistrationSerializer(serializers.ModelSerializer):
    registrationId = serializers.CharField(source='public_id', read_only=True)
    userId = serializers.SlugRelatedField(source='profile', read_only=True, slug_field='get_user_username')

    class Meta:
        model = SoloEventRegistration
        fields = ['registrationId', 'userId', 'status']


# This Serializer is To List all Registrations for a Solo Event
class SoloEventRegistrationsSerializer(serializers.ModelSerializer):
    eventPublicId = serializers.CharField(source='public_id', read_only=True)
    eventType = serializers.CharField(source='event_type', read_only=True)
    registrations = SoloEventRegistrationSerializer(source='soloeventregistration_set', many=True)

    class Meta:
        model = SoloEvent
        fields = ['eventPublicId', 'eventType', 'registrations']

