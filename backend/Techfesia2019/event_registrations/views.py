from accounts.models import Profile
from .models import Team
from .permissions import IsStaffUser, IsStaffUserOrPost
from .serializers import TeamSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# Team Views


class TeamDetailDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, public_id):
        try:
            return Team.objects.get(public_id=public_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team Doesn\'t Exist.'}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, public_id, format=None):
        team = self.get_object(public_id)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def delete(self, request, public_id, format=None):
        print(public_id)
        try:
            team = Team.objects.get(public_id=public_id)
            team.delete()
        except Team.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Team Deleted'}, status=status.HTTP_200_OK)


class TeamListCreateView(APIView):
    permission_classes = (IsStaffUserOrPost,)

    def get(self, request, format=None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            user = request.user
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = JSONParser().parse(request)
        team = Team(name=data['name'], team_leader=profile)
        team.save()
        data = TeamSerializer(team).data
        return Response(data, status=status.HTTP_201_CREATED)
