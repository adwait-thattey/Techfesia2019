from rest_framework import serializers
from .models import TicketComment, Ticket


class TicketSerializer(serializers.ModelSerializer):
    opened_by = serializers.SlugRelatedField(read_only=True, slug_field='get_user_username')
    solved_by = serializers.SlugRelatedField(read_only=True, slug_field='get_user_username')

    class Meta:
        model = Ticket
        fields = [
            'public_id', 'title', 'description',
            'opened_by', 'opening_date', 'status',
            'solved_by', 'solving_date', 'content'
        ]
