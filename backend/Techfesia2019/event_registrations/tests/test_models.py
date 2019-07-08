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

        self.profile = Profile.objects.create(user=self.user,
                                              college=self.institute,
                                              phone_number='+991234567890'
                                              )

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
        self.profile2 = Profile.objects.create(user=self.user2,
                                               college=self.institute,
                                               phone_number='+991234567891'
                                               )
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

        self.profile = Profile.objects.create(user=self.user,
                                              college=self.institute,
                                              phone_number='+991234567890'
                                              )

        self.profile2 = Profile.objects.create(user=self.user2,
                                               college=self.institute,
                                               phone_number='+991234567891'
                                               )

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

    def test_rejected_status(self):
        self.team_member.invitation_rejected = True
        self.team_member.invitation_accepted = False
        self.team_member.save()
        self.assertEqual(self.team_member.status, 'rejected')
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
