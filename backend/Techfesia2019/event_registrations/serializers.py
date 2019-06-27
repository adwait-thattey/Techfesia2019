from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    teammember_set = serializers.SlugRelatedField(many=True, read_only=True, slug_field='get_user_username')
    team_leader = serializers.SlugRelatedField(read_only=True, slug_field='get_user_username')
    invitees = serializers.SlugRelatedField(many=True, read_only=True, slug_field='get_user_username')
    events = serializers.SlugRelatedField(many=True, read_only=True, slug_field='get_event_public_id')

    class Meta:
        model = Team
        fields = ['public_id', 'name', 'team_leader', 'teammember_set', 'invitees', 'events']

    def is_valid(self, raise_exception=False):
        return super().is_valid()
