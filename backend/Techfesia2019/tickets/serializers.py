from rest_framework import serializers
from .models import TicketComment, Ticket


class TicketSerializer(serializers.ModelSerializer):
    opened_by = serializers.SlugRelatedField(read_only=True, slug_field='get_user_username')
    solved_by = serializers.SlugRelatedField(read_only=True, slug_field='get_user_username')
    subscribers = serializers.SlugRelatedField(many=True, read_only=True, slug_field='get_user_username')
    event = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Ticket
        fields = [
            'public_id', 'title', 'description',
            'opened_by', 'opening_date', 'status', 'event',
            'solved_by', 'solving_date', 'content', 'subscribers'
        ]


class TicketCommentSerializer(serializers.ModelSerializer):
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='public_id')
    commenter = serializers.SlugRelatedField(read_only=True, slug_field='get_user_username')

    class Meta:
        model = TicketComment
        fields = [
            'public_id', 'ticket', 'commenter',
            'text', 'posting_date'
        ]
