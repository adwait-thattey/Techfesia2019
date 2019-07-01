from accounts.models import Profile
from events.models import Event, TeamEvent
from .models import Team, TeamMember, TeamEventRegistration
from .permissions import IsStaffUser, IsStaffUserOrPost, IsAuthenticatedOrPost
from .serializers import TeamSerializer, TeamMemberSerializer, TeamEventRegistrationSerializer
from .serializers import TeamEventRegistrationsSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# Team Views


class TeamDetailEditDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, public_id):
        try:
            return Team.objects.get(public_id=public_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team Doesn\'t Exist.'}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, public_id, format=None):
        team = self.get_object(public_id)
        if team.leader is not request.user and not request.user.is_staff:
            return Response({'error': 'This is not your Team'}, status=status.HTTP_403_FORBIDDEN)
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, public_id, format=None):
        try:
            team = Team.objects.get(public_id=public_id)
            if team.leader is not request.user and not request.user.is_staff:
                return Response({'error': 'This Team is not yours to delete'}, status=status.HTTP_403_FORBIDDEN)
            team.delete()
        except Team.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Team Deleted'}, status=status.HTTP_200_OK)

    def put(self, request, public_id, format=None):
        team = self.get_object(public_id=public_id)
        if team.leader is not request.user and not request.user.is_staff:
            return Response({'error': 'This is not your Team'}, status=status.HTTP_403_FORBIDDEN)
        try:
            team.name = JSONParser().parse(request)['name']
            team.save()
        except KeyError:
            return Response({'message': 'required field "name" not provided'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(TeamSerializer(team).data, status=status.HTTP_200_OK)


class TeamListCreateView(APIView):
    permission_classes = (IsAuthenticatedOrPost,)

    def get(self, request, format=None):
        teams = Team.objects.all()
        if not request.user.is_staff:
            profile = Profile.objects.get(user=request.user)
            teams = teams.filter(team_leader=profile)
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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


class TeamInvitationListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username, format=None):
        if not request.user.username == username:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({'message': 'User Profile is not complete'}, status=status.HTTP_400_BAD_REQUEST)
        invitations = TeamMember.objects.filter(profile=profile)
        serializer = TeamMemberSerializer(invitations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamInvitationDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username, team_public_id, format=None):
        if not request.user.username == username:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({'message': 'User Profile is not complete'}, status=status.HTTP_400_BAD_REQUEST)
        invitation = TeamMember.objects.filter(profile=profile).get(team__public_id=team_public_id)
        serializer = TeamMemberSerializer(invitation)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamInvitationAcceptView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, username, team_public_id, format=None):
        if not request.user.username == username:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({'message': 'User Profile is not complete'}, status=status.HTTP_400_BAD_REQUEST)
        invitation = TeamMember.objects.filter(profile=profile).get(team__public_id=team_public_id)
        if invitation.invitation_accepted:
            return Response({'error': 'Already Accepted'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            invitation.invitation_accepted = True
            invitation.save()
        serializer = TeamMemberSerializer(invitation)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamInvitationRejectView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, username, team_public_id, format=None):
        if not request.user.username == username:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({'message': 'User Profile is not complete'}, status=status.HTTP_400_BAD_REQUEST)
        invitation = TeamMember.objects.filter(profile=profile).get(team__public_id=team_public_id)
        if invitation.invitation_rejected:
            return Response({'error': 'Already Rejected'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            invitation.invitation_rejected = True
            invitation.invitation_accepted = False
            invitation.save()
        serializer = TeamMemberSerializer(invitation)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamInvitationCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, public_id, format=None):
        try:
            username = dict(request.data)['username']
        except KeyError:
            return Response({'error': 'User/Profile does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        profile = Profile.objects.get(user__username=username)
        team = Team.objects.get(public_id=public_id)
        if TeamMember.objects.filter(team=team, profile=profile).count() is not 0:
            print(TeamMember)
            return Response({'error': 'User Already Invited '}, status=status.HTTP_400_BAD_REQUEST)
        if team.leader == request.user and profile:
            team_member = TeamMember()
            team_member.team = team
            team_member.profile = profile
            team_member.save()
            serializer = TeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'You do not have access to do this'},
                            status=status.HTTP_403_FORBIDDEN
                            )


class TeamInvitationDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, public_id, username, format=None):
        profile = Profile.objects.get(user__username=username)
        team = Team.objects.get(public_id=public_id)
        try:
            team_member = TeamMember.objects.get(team=team, profile=profile)
        except TeamMember.DoesNotExist:
            return Response({'error': 'Doesn\'t Exist'}, status=status.HTTP_204_NO_CONTENT)
        if not team_member.invitation_accepted and team.leader == request.user:
            team_member.delete()
            return Response({'message': 'Invitation Deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Already Accepted, Try Deleting Member'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class TeamMemberDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, public_id, username, format=None):
        profile = Profile.objects.get(user__username=username)
        team = Team.objects.get(public_id=public_id)
        try:
            team_member = TeamMember.objects.get(team=team, profile=profile, invitation_accepted=True)
        except TeamMember.DoesNotExist:
            return Response({'error': 'Doesn\'t Exist or Not accepted Invitation'}, status=status.HTTP_204_NO_CONTENT)
        if team.leader == request.user:
            team_member.delete()
            return Response({'message': 'Member Deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'You do not have the permission to do this'}, status=status.HTTP_403_FORBIDDEN)


class TeamEventRegistrationView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, public_id, format=None):
        try:
            base_event = Event.objects.get(public_id=public_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event does not exit'}, status=status.HTTP_400_BAD_REQUEST)
        data = JSONParser().parse(request)
        if base_event.team_event:  # Team Event Registration
            try:
                event = base_event.teamevent

            except TeamEvent.DoesNotExist:
                return Response({'error': 'The event is not a team Event'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            registration = TeamEventRegistration()
            registration.event = event

            try:
                team = Team.objects.get(public_id=data['team'])
                print(team.leader, request.user)
                if team.leader != request.user:
                    return Response({'error': 'Only Team Leader can register a Team for an event'},
                                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                                    )
                registration.team = team

            except KeyError as key:
                return Response({'error': '{0} is a required field.'.format(key)}, status=status.HTTP_400_BAD_REQUEST)

            except Team.DoesNotExist:
                return Response({'error': 'Team does not exit'}, status=status.HTTP_400_BAD_REQUEST)

            if TeamEventRegistration.objects.filter(team__team_leader__user=request.user, event=event).count() is not 0:
                registration = TeamEventRegistration.objects.filter(team__team_leader__user=request.user, event=event)
                serializer = TeamEventRegistrationSerializer(registration[0])
                return Response({'error': 'Already registered for event', 'registration_details': serializer.data},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY
                                )

            registration.save()
            serializer = TeamEventRegistrationSerializer(registration)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:  # Solo Event Registration TODO: SAYAM
            pass

        # serializer = TeamEventRegistrationSerializer(registration)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, public_id, format=None):
        try:
            base_event = Event.objects.get(public_id=public_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event does not exit'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            event = base_event.teamevent
        except TeamEvent.DoesNotExist:
            return Response({'error': 'The event is not a team Event'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            registration = TeamEventRegistration.objects.get(event=event, team__team_leader__user=request.user)
        except TeamEventRegistration.DoesNotExist:
            return Response({'error': 'Not Registered for Event'}, status=status.HTTP_204_NO_CONTENT)
        registration.delete()
        return Response({'message': 'unregistered from event'}, status=status.HTTP_200_OK)


class TeamEventRegistrationListView(APIView):
    permission_classes = (IsStaffUser,)

    def get(self, request, public_id, format=None):
        try:
            base_event = Event.objects.get(public_id=public_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event does not exit'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            event = base_event.teamevent
        except TeamEvent.DoesNotExist:
            return Response({'error': 'The event is not a team Event'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        serializer = TeamEventRegistrationsSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamEventRegistrationDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, public_id, format=None):
        try:
            base_event = Event.objects.get(public_id=public_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event does not exit'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            event = base_event.teamevent
        except TeamEvent.DoesNotExist:
            return Response({'error': 'The event is not a team Event'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            registration = TeamEventRegistration.objects.get(event=event, team__team_leader__user=request.user)
        except TeamEventRegistration.DoesNotExist:
            return Response({'error': 'User is Not Registered'}, status=status.HTTP_204_NO_CONTENT)
        serializer = TeamEventRegistrationSerializer(registration)
        return Response(serializer.data, status=status.HTTP_200_OK)