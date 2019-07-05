from accounts.models import Profile
from events.models import Event, TeamEvent, SoloEvent
from .models import Team, TeamMember, TeamEventRegistration, SoloEventRegistration
from .permissions import IsStaffUser, IsStaffUserOrPost, IsAuthenticatedOrPost
from .serializers import TeamSerializer, TeamMemberSerializer, TeamEventRegistrationSerializer, SoloEventRegistrationSerializer
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
        print(team.leader, request.user)
        if team.leader != request.user and not request.user.is_staff:
            return Response({'error': 'This is not your Team'}, status=status.HTTP_403_FORBIDDEN)
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, public_id, format=None):
        try:
            team = Team.objects.get(public_id=public_id)
            if team.leader != request.user and not request.user.is_staff:
                return Response({'error': 'This Team is not yours to delete'}, status=status.HTTP_403_FORBIDDEN)
            if team.events.count() == 0:
                return Response({'error': 'Can\'t delete a registered team.'}, status=status.HTTP_403_FORBIDDEN)
            team.delete()
        except Team.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Team Deleted'}, status=status.HTTP_200_OK)

    def put(self, request, public_id, format=None):
        team = self.get_object(public_id=public_id)
        if team.leader != request.user and not request.user.is_staff:
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
        if team.events.count() is not 0:
            return Response({'error': 'Can\'t add member to a registered team'})
        if TeamMember.objects.filter(team=team, profile=profile).count() is not 0:
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
        if team.events.count() is not 0:
            return Response({'error': 'Can\'t remove member from a registered team'})
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
        # 1. Get Event (check if wrong event type)
        try:
            base_event = Event.objects.get(public_id=public_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event does not exit'}, status=status.HTTP_400_BAD_REQUEST)
        data = JSONParser().parse(request)

        # For Team Events
        if base_event.team_event:
        # 1. Get Team Event Model
            try:
                event = base_event.teamevent
            except TeamEvent.DoesNotExist:
                return Response({'error': 'The event is not a team Event'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        # 2. Get Team Details (verify team size, leader)
            try:
                team = Team.objects.get(public_id=data['team'])
                print(team.leader, request.user)
                if team.leader != request.user:
                    return Response({'error': 'Only Team Leader can register a Team for an event'},
                                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                                    )
            except KeyError as key:
                return Response({'error': '{0} is a required field.'.format(key)}, status=status.HTTP_400_BAD_REQUEST)

            except Team.DoesNotExist:
                return Response({'error': 'Team does not exit'}, status=status.HTTP_400_BAD_REQUEST)

        # 3. Check for existing registration
            team_members = [team.team_leader.user, ] + [i.profile.user for i in team.teammember_set.all()]
            for i in team_members:
                if event.find_registration(user=i).count() is not 0:
                    serializer = TeamEventRegistrationSerializer(event.find_registration(user=i), many=True)
                    return Response({'error': 'Already registered for event', 'registration_details': serializer.data},
                                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                                    )
        # 4. Register Team
            registration = TeamEventRegistration()
            registration.team = team
            registration.event = event
            registration.is_reserved = team.is_reserved
            registration.save()
            serializer = TeamEventRegistrationSerializer(registration)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # For Solo Events:
        else:
            # 1. Get Solo Event Model
            try:
                event = base_event.soloevent
            except SoloEvent.DoesNotExist:
                return Response({'error': 'The event is not a Solo Event'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            # 2. Get User Profile Details
            try:
                profile = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                return Response({'error': 'User Profile do not exist or incomplete'}, status=status.HTTP_404_NOT_FOUND)

            # 3. Check for existing registration
            if SoloEventRegistration.objects.filter(profile=profile, event=event).count() is not 0:
                registration = SoloEventRegistration.objects.filter(profile=profile, event=event)[0]
                serializer = SoloEventRegistrationSerializer(registration)
                return Response({'error': 'Already registered for event', 'registration_details': serializer.data},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY
                                )
            # 4. Register Person
            registration = SoloEventRegistration()
            registration.profile = profile
            registration.event = event
            registration.is_reserved = (profile.college.name == 'Indian Institute of Information Technology, Sri City')
            registration.save()
            serializer = SoloEventRegistrationSerializer(registration)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # TODO: Refresh Waiting List for Events

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