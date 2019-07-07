from django.test import TestCase
from event_registrations.models import Team, TeamMember
from accounts.models import Profile, Institute
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
        self.assertEqual(self.team.create_date, dt.datetime.now(tz=self.team.create_date.tzinfo))

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
        self.assertEqual(self.team_member.status, 'rejected')
        self.assertFalse(self.team.members.filter(profile=self.profile2).exists())
        self.assertTrue(self.team.invitees.filter(profile=self.profile2).exists())

    def test_accepted_status(self):
        self.team_member.invitation_accepted = True
        self.assertEqual(self.team_member.status, 'accepted')
        self.assertTrue(self.team.members.filter(profile=self.profile2).exists())
        self.assertFalse(self.team.invitees.filter(profile=self.profile2).exists())

