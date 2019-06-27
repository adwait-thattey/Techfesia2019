from django.shortcuts import render
from rest_framework.views import APIView
from .models import Team
from .serializers import TeamSerializer
from rest_framework.response import Response
# Create your views here.

# Team Views


class TeamDetailView(APIView):
    def get_object(self, public_id):
        try:
            return Team.objects.get(public_id=public_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team Doesn\'t Exist.'})

    def get(self, request, public_id, format=None):
        team = self.get_object(public_id)
        serializer = TeamSerializer(team)
        return Response(serializer.data)


