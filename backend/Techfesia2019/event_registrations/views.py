from django.db import IntegrityError
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from registration.models import User
from accounts.models import Profile
from events.models import Event, TeamEvent, SoloEvent
from .models import Team, TeamMember, TeamEventRegistration, SoloEventRegistration
from .permissions import IsStaffUser, IsAuthenticatedOrPost
from .serializers import SoloEventRegistrationSerializer, SoloEventRegistrationsSerializer
from .serializers import TeamEventRegistrationsSerializer
from .serializers import TeamSerializer, TeamMemberSerializer, TeamEventRegistrationSerializer


class TeamDetailEditDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, public_id, format=None):
        try:
            team = Team.objects.get(public_id=public_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team Doesn\'t Exist.'}, status=status.HTTP_204_NO_CONTENT)
        if team.leader != request.user and not request.user.is_staff:
            return Response({'error': 'This is not your Team'}, status=status.HTTP_403_FORBIDDEN)
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, public_id, format=None):
        try:
            team = Team.objects.get(public_id=public_id)
            if team.leader != request.user and not request.user.is_staff:
                return Response({'error': 'This Team is not yours to delete'}, status=status.HTTP_403_FORBIDDEN)
            if team.events.count() is not 0:
                return Response({'error': 'Can\'t delete a registered team.'},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY
                                )
            # Cleaning up TeamMembers models
            for member in TeamMember.objects.filter(team=team):
                member.delete()
            team.delete()
        except Team.DoesNotExist:
            return Response({'error': 'Team does not exist'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Team Deleted'}, status=status.HTTP_200_OK)

    def put(self, request, public_id, format=None):
        try:
            team = Team.objects.get(public_id=public_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team Doesn\'t Exist.'}, status=status.HTTP_204_NO_CONTENT)
        if team.leader != request.user and not request.user.is_staff:
            return Response({'error': 'This is not your Team'}, status=status.HTTP_403_FORBIDDEN)
        try:
            team.name = JSONParser().parse(request)['name']
            team.save()
        except KeyError:
            return Response({'message': 'required field "name" not provided'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({'message': 'required field "name" already in use'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(TeamSerializer(team).data, status=status.HTTP_200_OK)


class TeamListCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        teams = Team.objects.all()
        if not request.user.is_staff:
            try:
                profile = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                return Response({'error': 'Profile not complete'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            teams = teams.filter(team_leader=profile)
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            user = request.user
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not complete'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        data = JSONParser().parse(request)
        try:
            team = Team(name=data['name'], team_leader=profile)
            team.save()
        except KeyError:
            return Response({'message': 'required field "name" not provided'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({'message': 'required field "name" already in use'}, status=status.HTTP_400_BAD_REQUEST)

        data = TeamSerializer(team).data
        return Response(data, status=status.HTTP_201_CREATED)


class TeamInvitationListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username, format=None):
        if not request.user.username == username:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({'message': 'User Profile is not complete'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        invitations = TeamMember.objects.filter(profile=profile)
        serializer = TeamMemberSerializer(invitations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamInvitationDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username, team_public_id, format=None):
        if not request.user.username == username:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({'message': 'User Profile is not complete'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            invitation = TeamMember.objects.filter(profile=profile).get(team__public_id=team_public_id)
        except TeamMember.DoesNotExist:
            return Response({'message': 'you have no invitations'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TeamMemberSerializer(invitation)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamInvitationAcceptView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, username, team_public_id, format=None):
        if not request.user.username == username:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({'message': 'User Profile is not complete'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            invitation = TeamMember.objects.filter(profile=profile).get(team__public_id=team_public_id)
        except TeamMember.DoesNotExist:
            return Response({'error': 'Invitation not found'}, status=status.HTTP_404_NOT_FOUND)
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
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({'message': 'User Profile is not complete'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            invitation = TeamMember.objects.filter(profile=profile).get(team__public_id=team_public_id)
        except TeamMember.DoesNotExist:
            return Response({'error': 'Invitation not found'}, status=status.HTTP_404_NOT_FOUND)
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
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
        except KeyError:
            return Response({'error': '"username" key not provided'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile is not complete'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            team = Team.objects.get(public_id=public_id)
        except Team.DoesNotExist:
            return Response({'error': 'Team does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if team.events.count() is not 0:
            return Response({'error': 'Can\'t add member to a registered team'})
        if TeamMember.objects.filter(team=team, profile=profile).count() is not 0:
            return Response({'error': 'User Already Invited '}, status=status.HTTP_400_BAD_REQUEST)
        if team.leader == request.user and profile:
            if team.team_leader == profile:
                return Response({'error': 'You can not invite yourself'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
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
        try:
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
        except User.DoesNotExist:
            return Response({'error': 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile is not complete'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            team = Team.objects.get(public_id=public_id)
        except Team.DoesNotExist:
            return Response({'error': 'Team does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if not request.user == team.team_leader.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            team_member = TeamMember.objects.get(team=team, profile=profile)
        except TeamMember.DoesNotExist:
            return Response({'error': 'Doesn\'t Exist'}, status=status.HTTP_204_NO_CONTENT)
        if not team_member.invitation_accepted and team.leader == request.user:
            team_member.delete()
            return Response({'message': 'Invitation Deleted'}, status=status.HTTP_200_OK)
        return Response({'error': 'Already Accepted, Try Deleting Member'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class TeamMemberDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, public_id, username, format=None):
        try:
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            team = Team.objects.get(public_id=public_id)
        except Team.DoesNotExist:
            return Response({'error': 'Team does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if team.events.count() is not 0:
            return Response({'error': 'Can\'t remove member from a registered team'},
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY
                            )
        try:
            team_member = TeamMember.objects.get(team=team, profile=profile, invitation_accepted=True)
        except TeamMember.DoesNotExist:
            return Response({'error': 'Doesn\'t Exist or Not accepted Invitation'}, status=status.HTTP_204_NO_CONTENT)
        if team.leader == request.user:
            team_member.delete()
            return Response({'message': 'Member Deleted'}, status=status.HTTP_200_OK)
        return Response({'error': 'You do not have the permission to do this'}, status=status.HTTP_403_FORBIDDEN)


class EventRegistrationView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, public_id, format=None):
        # 1. Get Event (check if wrong event type)
        try:
            base_event = Event.objects.get(public_id=public_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event does not exit'}, status=status.HTTP_400_BAD_REQUEST)

        # For Team Events
        if base_event.team_event:
            # 1. Get Team Event Model
            try:
                event = base_event.teamevent
            except TeamEvent.DoesNotExist:
                return Response({'error': 'The event is not a team Event'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            # 2. Get Team Details (verify team size, leader)
            data = JSONParser().parse(request)
            try:
                team = Team.objects.get(public_id=data['team'])
                if team.leader != request.user:
                    return Response({'error': 'Only Team Leader can register a Team for an event'},
                                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                                    )
            except KeyError as key:
                return Response({'error': '{0} is a required field.'.format(key)}, status=status.HTTP_400_BAD_REQUEST)

            except Team.DoesNotExist:
                return Response({'error': 'Team does not exit'}, status=status.HTTP_404_NOT_FOUND)

            if event.min_team_size <= team.member_count <= event.max_team_size:
                pass
            else:
                return Response({'error': 'Team size is not '}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            if not team.ready():
                return Response({'error': 'Team has pending invitations'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            # 3. Check for existing registration
            team_members = [team.team_leader.user, ] + [i.profile.user for i in team.teammember_set.all()]
            for i in team_members:
                if event.find_registration(user=i) is not None:
                    serializer = TeamEventRegistrationSerializer(event.find_registration(user=i))
                    return Response({'error': 'Already registered for event', 'registration_details': serializer.data},
                                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                                    )
            # 4. Register Team
            registration = TeamEventRegistration()
            registration.team = team
            registration.event = event
            registration.is_reserved = team.is_reserved
            registration.save()
            event.refresh_participants()  # Refreshing registrations
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
            try:
                registration.is_reserved = \
                    (profile.college.name == 'Indian Institute of Information Technology, Sri City')
            except AttributeError:
                registration.is_reserved = False
            registration.save()
            event.refresh_participants()  # Refreshing registrations
            serializer = SoloEventRegistrationSerializer(registration)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, public_id, format=None):
        try:
            base_event = Event.objects.get(public_id=public_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event does not exit'}, status=status.HTTP_400_BAD_REQUEST)
        if base_event.team_event:
            try:
                event = base_event.teamevent
            except TeamEvent.DoesNotExist:
                return Response({'error': 'The event doesn\'t exist'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            registration = event.find_registration(request.user)
            if registration is not None:
                if registration.team.leader == request.user:
                    registration.delete()
                    event.refresh_participants()  # Refreshing registrations
                else:
                    return Response({'error': 'You are not the leader'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                return Response({'message': 'Successfully unregistered from event'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Not Registered for Event'}, status=status.HTTP_204_NO_CONTENT)

        else:
            try:
                event = base_event.soloevent
            except SoloEvent.DoesNotExist:
                return Response({'error': 'The event doesn\'t exist'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            try:
                registration = SoloEventRegistration.objects.get(event=event, profile=request.user.profile)
            except SoloEventRegistration.DoesNotExist:
                return Response({'error': 'Not Registered for Event'}, status=status.HTTP_204_NO_CONTENT)
            registration.delete()
            event.refresh_participants()  # Refreshing registrations
            return Response({'message': 'Successfully unregistered from event'}, status=status.HTTP_200_OK)


class EventRegistrationListView(APIView):
    permission_classes = (IsStaffUser,)

    def get(self, request, public_id, format=None):
        try:
            base_event = Event.objects.get(public_id=public_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event does not exit'}, status=status.HTTP_404_NOT_FOUND)
        if base_event.team_event:
            try:
                event = base_event.teamevent
            except TeamEvent.DoesNotExist:
                return Response({'error': 'The event Doesn\'t exist'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            serializer = TeamEventRegistrationsSerializer(event)
        else:
            try:
                event = base_event.soloevent
            except TeamEvent.DoesNotExist:
                return Response({'error': 'The event Doesn\'t exist'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            serializer = SoloEventRegistrationsSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EventRegistrationDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, public_id, format=None):
        try:
            base_event = Event.objects.get(public_id=public_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event does not exit'}, status=status.HTTP_400_BAD_REQUEST)
        if base_event.team_event:
            try:
                event = base_event.teamevent
            except TeamEvent.DoesNotExist:
                return Response({'error': 'The event Doesn\'t exist'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            if event.find_registration(user=request.user) is None:
                return Response({'error': 'User is Not Registered'}, status=status.HTTP_204_NO_CONTENT)
            else:
                registration = event.find_registration(user=request.user)
            serializer = TeamEventRegistrationSerializer(registration)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                event = base_event.soloevent
            except SoloEvent.DoesNotExist:
                return Response({'error': 'The event Doesn\'t exist'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            try:
                registration = SoloEventRegistration.objects.get(event=event, profile=request.user.profile)
            except SoloEventRegistration.DoesNotExist:
                return Response({'error': 'User is Not Registered'}, status=status.HTTP_204_NO_CONTENT)
            serializer = SoloEventRegistrationSerializer(registration)
            return Response(serializer.data, status=status.HTTP_200_OK)
