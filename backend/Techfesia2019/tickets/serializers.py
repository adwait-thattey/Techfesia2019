from rest_framework import serializers
from .models import TicketComment, Ticket


class TicketSerializer(serializers.ModelSerializer):
    publicId = serializers.CharField(source='public_id', read_only=True)
    openedBy = serializers.SlugRelatedField(source='owned_by', read_only=True, slug_field='get_user_username')
    solvedBy = serializers.SlugRelatedField(source='solved_by', read_only=True, slug_field='get_user_username')
    openingDate = serializers.DateField(source='opening_date')
    solvingDate = serializers.DateField(source='solving_date')
    subscribers = serializers.SlugRelatedField(many=True, read_only=True, slug_field='get_user_username')
    event = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Ticket
        fields = [
            'publicId', 'title', 'description',
            'openedBy', 'openingDate', 'status', 'event',
            'solvedBy', 'solvingDate', 'content', 'subscribers'
        ]


class TicketCommentSerializer(serializers.ModelSerializer):
    publicId = serializers.CharField(source='public_id', read_only=True)
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='public_id')
    commenter = serializers.SlugRelatedField(read_only=True, slug_field='get_user_username')
    postingDate = serializers.DateTimeField(source='posting_date')

    class Meta:
        model = TicketComment
        fields = [
            'publicId', 'ticket', 'commenter',
            'text', 'postingDate'
        ]
