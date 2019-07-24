from django.test import TestCase
from event_registrations.models import Team, TeamMember, SoloEventRegistration, TeamEventRegistration
from accounts.models import Profile, Institute
from events.models import SoloEvent, TeamEvent
from registration.models import User
import datetime as dt


# Team Model TestCase

class TeamTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )

        self.institute = Institute.objects.create()

        self.profile = Profile.objects.get(user=self.user)
        self.profile.college = self.institute
        self.profile.save()

        self.team = Team.objects.create(team_leader=self.profile,
                                        name='Sample Team1'
                                        )

    def test_model_creation(self):
        self.assertTrue(Team.objects.filter(team_leader=self.profile, name='Sample Team1').exists())

    def test_team_create_date(self):
        self.assertGreaterEqual(self.team.create_date,
                                dt.datetime.now(tz=self.team.create_date.tzinfo) - dt.timedelta(0, 5, 0))

    def test_reservation_status(self):
        self.assertTrue(self.team.is_reserved)

        self.user2 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user2',
                                         email='sampleuser2@test.com'
                                         )
        self.profile2 = Profile.objects.get(user=self.user2)
        self.profile2.college = self.institute
        self.profile2.save()
        self.institute2 = Institute.objects.create(name='Sample Institute 2')
        self.team_member = TeamMember.objects.create(team=self.team, profile=self.profile2)

        self.assertTrue(self.team.is_reserved)

        self.profile2.college = self.institute2
        self.profile2.save()

        self.assertFalse(self.team.is_reserved)

        self.profile = self.institute2
        self.profile.save()

        self.assertFalse(self.team.is_reserved)

        self.team_member.profile.college = self.institute

        self.assertFalse(self.team.is_reserved)


class TeamMemberTestCase(TestCase):
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

        self.institute = Institute.objects.create()

        self.profile = Profile.objects.get(user=self.user)
        self.profile.college = self.institute
        self.profile.save()

        self.profile2 = Profile.objects.get(user=self.user2)
        self.profile2.college = self.institute
        self.profile2.save()

        self.team = Team.objects.create(team_leader=self.profile,
                                        name='Sample Team1'
                                        )

        self.team_member = TeamMember.objects.create(team=self.team, profile=self.profile2)

    def test_model_creation(self):
        self.assertTrue(TeamMember.objects.filter(team=self.team, profile=self.profile2).exists())

    def test_team_member_from_team(self):
        self.assertTrue(self.team.teammember_set.filter(profile=self.profile2).exists())

    def test_team_leader(self):
        self.assertEqual(self.team_member.leader, self.profile)

    def test_member_status(self):
        self.assertEqual(self.team_member.status, 'pending')
        self.assertFalse(self.team.members.filter(profile=self.profile2).exists())
        self.assertTrue(self.team.invitees.filter(profile=self.profile2).exists())

    def test_accepted_status(self):
        self.team_member.invitation_accepted = True
        self.team_member.save()
        self.assertEqual(self.team_member.status, 'accepted')
        self.assertTrue(self.team.members.filter(profile=self.profile2).exists())
        self.assertFalse(self.team.invitees.filter(profile=self.profile2).exists())

    def test_team_size(self):
        self.assertEqual(self.team.member_count, 1)
        self.team_member.invitation_accepted = True
        self.team_member.save()
        self.assertEqual(self.team.member_count, 2)

    def test_team_ready(self):
        self.assertFalse(self.team.ready(), 0)
        self.team_member.invitation_accepted = True
        self.team_member.save()
        self.assertTrue(self.team.ready())


class SoloEventRegistrationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )

        self.institute = Institute.objects.create()

        self.profile = Profile.objects.get(user=self.user)
        self.profile.college = self.institute
        self.profile.save()

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

    def test_model_creation(self):
        self.assertTrue(SoloEventRegistration.objects.filter(event=self.event, profile=self.profile).exists())

    def test_is_reserved(self):
        self.assertEqual(self.registration.is_reserved, True)

    def test_is_confirmed(self):
        self.assertFalse(self.registration.is_confirmed)

    def test_is_complete(self):
        self.assertFalse(self.registration.is_complete)

    def test_created_on(self):
        self.assertGreaterEqual(self.registration.created_on,
                                dt.datetime.now(tz=self.registration.created_on.tzinfo) - dt.timedelta(0, 5, 0))

    def test_status(self):
        self.assertEqual(self.registration.status, 'payment pending')
        self.registration.is_complete = True
        self.registration.save()
        self.assertEqual(self.registration.status, 'waiting')
        self.registration.is_confirmed = True
        self.registration.save()
        self.assertEqual(self.registration.status, 'confirmed')


class TeamEventRegistrationTestCase(TestCase):
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

        self.profile = Profile.objects.get(user=self.user)
        self.profile.college = self.institute
        self.profile.save()
        self.profile1 = Profile.objects.get(user=self.user1)
        self.profile1.college = self.institute
        self.profile1.save()
        self.profile2 = Profile.objects.get(user=self.user2)
        self.profile2.college = self.institute
        self.profile2.save()

        self.event = TeamEvent.objects.create(title='Sample Solo Event',
                                              start_date=dt.date(2019, 7, 1),
                                              end_date=dt.date(2019, 7, 1),
                                              start_time=dt.time(12, 0, 0),
                                              end_time=dt.time(15, 0, 0),
                                              max_team_size=4,
                                              min_team_size=2
                                              )

        self.team = Team.objects.create(team_leader=self.profile,
                                        name='Sample Team1'
                                        )

        self.team_member1 = TeamMember.objects.create(team=self.team, profile=self.profile1, invitation_accepted=True)
        self.team_member2 = TeamMember.objects.create(team=self.team, profile=self.profile2, invitation_accepted=True)

        self.registration = TeamEventRegistration.objects.create(team=self.team, event=self.event,
                                                                 is_reserved=self.team.is_reserved
                                                                 )

    def test_model_creation(self):
        self.assertTrue(TeamEventRegistration.objects.filter(event=self.event, team=self.team).exists())

    def test_is_reserved(self):
        self.assertEqual(self.registration.is_reserved, True)

    def test_is_confirmed(self):
        self.assertFalse(self.registration.is_confirmed)

    def test_is_complete(self):
        self.assertFalse(self.registration.is_complete)

    def test_created_on(self):
        self.assertGreaterEqual(self.registration.created_on,
                                dt.datetime.now(tz=self.registration.created_on.tzinfo) - dt.timedelta(0, 5, 0))

    def test_status(self):
        self.assertEqual(self.registration.status, 'payment pending')
        self.registration.is_complete = True
        self.registration.save()
        self.assertEqual(self.registration.status, 'waiting')
        self.registration.is_confirmed = True
        self.registration.save()
        self.assertEqual(self.registration.status, 'confirmed')


class EventRefreshParticipantsTestCase(TestCase):
    def setUp(self):
        self.institute = Institute.objects.create()
        self.institute1 = Institute.objects.create(name='Other Institute')
        self.event = SoloEvent.objects.create(title='Sample Solo Event1',
                                              start_date=dt.date(2019, 8, 3),
                                              start_time=dt.time(12, 0, 0),
                                              end_date=dt.date(2019, 9, 4),
                                              end_time=dt.time(10, 0, 0),
                                              max_participants=15,
                                              reserved_slots=5
                                              )
        self.event1 = SoloEvent.objects.create(title='Sample Solo Event2',
                                               start_date=dt.date(2019, 8, 3),
                                               start_time=dt.time(12, 0, 0),
                                               end_date=dt.date(2019, 9, 4),
                                               end_time=dt.time(10, 0, 0),
                                               max_participants=18,
                                               reserved_slots=12
                                               )

        self.users = []
        self.profiles = []

        for i in range(1, 11):
            user = User.objects.create(username='sample_test_user' + str(i),
                                       first_name='sample',
                                       last_name='user' + str(i),
                                       email='sample_user{0}@test.com'.format(str(i)),
                                       email_confirmed=True
                                       )
            profile = Profile.objects.get(user=user)
            profile.college = self.institute
            profile.save()
            self.users.append(user)
            self.profiles.append(profile)

            SoloEventRegistration.objects.create(event=self.event, profile=profile,
                                                 is_complete=True, is_reserved=False
                                                 )
            SoloEventRegistration.objects.create(event=self.event1, profile=profile,
                                                 is_complete=True, is_reserved=False
                                                 )

        for i in range(11, 21):
            user = User.objects.create(username='sample_test_user' + str(i),
                                       first_name='sample',
                                       last_name='user' + str(i),
                                       email='sample_user{0}@test.com'.format(str(i)),
                                       email_confirmed=True
                                       )
            profile = Profile.objects.get(user=user)
            profile.college = self.institute1
            profile.save()
            self.users.append(user)
            self.profiles.append(profile)

            SoloEventRegistration.objects.create(event=self.event, profile=profile,
                                                 is_complete=True, is_reserved=True
                                                 )
            SoloEventRegistration.objects.create(event=self.event1, profile=profile,
                                                 is_complete=True, is_reserved=True
                                                 )

    def test_refresh_participants(self):
        self.event.refresh_participants()
        self.event1.refresh_participants()
        self.assertGreaterEqual(self.event.current_reserved_participants().count(), 5)
        self.assertLessEqual(self.event.current_participants().filter(is_reserved=False).count(), 10)
        self.assertLessEqual(self.event1.current_reserved_participants().count(), 12)
        self.assertLessEqual(self.event1.current_participants().count(), 18)
