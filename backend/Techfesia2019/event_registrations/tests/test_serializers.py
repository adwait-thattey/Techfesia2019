from django.test import TestCase
from registration.models import User
from accounts.models import Profile, Institute
from events.models import SoloEvent
from event_registrations.models import Team, TeamMember, SoloEventRegistration
from event_registrations.serializers import TeamSerializer, TeamMemberSerializer, SoloEventRegistrationSerializer
import datetime as dt


class TeamSerializerTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user1',
                                        email='sampleuser1@test.com'
                                        )

        self.user2 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user2',
                                         email='sampleuser2@test.com'
                                         )
        self.user3 = User.objects.create(username='sample_test_user3',
                                         first_name='sample',
                                         last_name='user3',
                                         email='sampleuser3@test.com'
                                         )

        self.institute = Institute.objects.create()

        self.profile = Profile.objects.create(user=self.user,
                                              college=self.institute,
                                              phone_number='+991234567890'
                                              )

        self.profile2 = Profile.objects.create(user=self.user2,
                                               college=self.institute,
                                               phone_number='+991234567891'
                                               )

        self.profile3 = Profile.objects.create(user=self.user3,
                                               college=self.institute,
                                               phone_number='+991234567892'
                                               )

        self.team = Team.objects.create(team_leader=self.profile,
                                        name='Sample Team1'
                                        )

        self.team_member = TeamMember.objects.create(team=self.team, profile=self.profile2)
        self.team_member2 = TeamMember.objects.create(team=self.team, profile=self.profile3, invitation_accepted=True)

        self.test_data = {
            'teamId': self.team.public_id,
            'name': 'Sample Team1',
            'leader': 'sample_test_user1',
            'members': ['sample_test_user3'],
            'invitees': ['sample_test_user2'],
            'events': [],
        }
        self.serializer = TeamSerializer(instance=self.team)

    def test_contains_all_fields(self):
        self.assertCountEqual(set(self.serializer.data.keys()), set(self.test_data.keys()))

    def test_team_name(self):
        self.assertEqual(self.test_data['name'], self.serializer['name'].value)

    def test_check_leader(self):
        self.assertEqual(self.test_data['leader'], self.serializer['leader'].value)

    def test_check_team_id(self):
        self.assertEqual(self.test_data['teamId'], self.serializer['teamId'].value)

    def test_check_invitees(self):
        self.assertEqual(self.test_data['invitees'], self.serializer['invitees'].value)

    def test_check_members(self):
        self.assertEqual(self.test_data['members'], self.serializer['members'].value)

    def test_events(self):
        self.assertEqual(self.test_data['events'], self.serializer['events'].value)


class TeamMemberSerializerTestCase(TestCase):
    # Used in Team Invitation Views
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user1',
                                        email='sampleuser1@test.com'
                                        )

        self.user1 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user2',
                                         email='sampleuser2@test.com'
                                         )
        self.user2 = User.objects.create(username='sample_test_user3',
                                         first_name='sample',
                                         last_name='user3',
                                         email='sampleuser3@test.com'
                                         )

        self.institute = Institute.objects.create()

        self.profile = Profile.objects.create(user=self.user,
                                              college=self.institute,
                                              phone_number='+991234567890'
                                              )

        self.profile1 = Profile.objects.create(user=self.user1,
                                               college=self.institute,
                                               phone_number='+991234567891'
                                               )

        self.profile2 = Profile.objects.create(user=self.user2,
                                               college=self.institute,
                                               phone_number='+991234567892'
                                               )

        self.team = Team.objects.create(team_leader=self.profile,
                                        name='Sample Team1'
                                        )

        self.team_member1 = TeamMember.objects.create(team=self.team, profile=self.profile1)
        self.team_member2 = TeamMember.objects.create(team=self.team, profile=self.profile2, invitation_accepted=True)

        self.test_data1 = {
            'teamId': self.team_member1.team.public_id,
            'name': 'Sample Team1',
            'leader': 'sample_test_user1',
            'status': 'pending',
        }
        self.test_data2 = {
            'teamId': self.team_member2.team.public_id,
            'name': 'Sample Team1',
            'leader': 'sample_test_user1',
            'status': 'accepted',
        }

        self.serializer1 = TeamMemberSerializer(instance=self.team_member1)
        self.serializer2 = TeamMemberSerializer(instance=self.team_member2)

    def test_contains_all_fields(self):
        self.assertCountEqual(set(self.serializer1.data.keys()), set(self.test_data1.keys()))
        self.assertCountEqual(set(self.serializer2.data.keys()), set(self.test_data2.keys()))

    def test_team_name(self):
        self.assertEqual(self.test_data1['name'], self.serializer1['name'].value)
        self.assertEqual(self.test_data2['name'], self.serializer2['name'].value)

    def test_team_leader(self):
        self.assertEqual(self.test_data1['leader'], self.serializer1['leader'].value)
        self.assertEqual(self.test_data2['leader'], self.serializer2['leader'].value)

    def test_team_id(self):
        self.assertEqual(self.test_data1['teamId'], self.serializer1['teamId'].value)
        self.assertEqual(self.test_data2['teamId'], self.serializer2['teamId'].value)

    def test_team_status(self):
        self.assertEqual(self.test_data1['status'], self.serializer1['status'].value)
        self.assertEqual(self.test_data2['status'], self.serializer2['status'].value)


class SoloEventRegistrationSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )

        self.institute = Institute.objects.create()

        self.profile = Profile.objects.create(user=self.user,
                                              college=self.institute,
                                              phone_number='+991234567890'
                                              )

        self.event = SoloEvent.objects.create(title='Sample Solo Event',
                                              start_date=dt.date(2019, 7, 1),
                                              end_date=dt.date(2019, 7, 1),
                                              start_time=dt.time(12, 0, 0),
                                              end_time=dt.time(15, 0, 0)
                                              )
        is_reserved = self.profile.college.name == 'Indian Institute of Information Technology, Sri City'
        self.registration = SoloEventRegistration.objects.create(event=self.event,
                                                                 profile=self.profile,
                                                                 is_reserved=is_reserved,
                                                                 )
        self.serializer = SoloEventRegistrationSerializer(instance=self.registration)
        self.test_data = {
            'registrationId': self.registration.public_id,
            'userId': 'sample_test_user1',
            'status': 'payment pending',
        }

    def test_contains_all_fields(self):
        self.assertCountEqual(set(self.serializer.data.keys()), set(self.test_data.keys()))

    def test_registration_id(self):
        self.assertEqual(self.test_data['registrationId'], self.serializer['registrationId'].value)

    def test_user_id(self):
        self.assertEqual(self.test_data['userId'], self.serializer['userId'].value)

    def test_status(self):
        self.assertEqual(self.test_data['status'], self.serializer['status'].value)

