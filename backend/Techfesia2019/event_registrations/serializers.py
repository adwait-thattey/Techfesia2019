from rest_framework import serializers
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
