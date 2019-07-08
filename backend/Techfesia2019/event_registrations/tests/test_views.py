from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from registration.models import User
from accounts.models import Institute, Profile
from events.models import TeamEvent
from event_registrations.models import Team, TeamMember, TeamEventRegistration
# from event_registrations.views import TeamListCreateView, TeamDetailEditDeleteView
import json
import datetime as dt


class TeamDetailEditDeleteViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )
        self.user1 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user2',
                                         email='sampleuser2@test.com'
                                         )
        self.staff_user = User.objects.create(username='staff',
                                              first_name = 'staff',
                                              last_name = 'user',
                                              email = 'staff@test.com',
                                              is_staff = True
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
        self.team1 = Team.objects.create(team_leader=self.profile1,
                                         name='Sample Team2'
                                         )

        self.team_member1 = TeamMember.objects.create(team=self.team, profile=self.profile1, invitation_accepted=True)

        self.registration = TeamEventRegistration.objects.create(team=self.team, event=self.event,
                                                                 is_reserved=self.team.is_reserved
                                                                 )

    def test_team_detail_view_unauthenticated(self):
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.login(user=None)  # self.client.logout()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_team_detail_view_wrong_user(self):
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.force_login(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_team_detail_view_team_does_not_exist(self):
        url = reverse('team_details', args=('random_string',))
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_team_detail_view(self):
        test_data = {
            'teamId': self.team.public_id,
            'name': 'Sample Team1',
            'leader': 'sample_test_user1',
            'members': ['sample_test_user2'],
            'invitees': [],
            'events': [],
        }
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['teamId'], test_data['teamId'])
        self.assertEqual(response.data['name'], test_data['name'])
        self.assertEqual(response.data['leader'], test_data['leader'])
        self.assertEqual(response.data['members'], test_data['members'])
        self.assertEqual(response.data['invitees'], test_data['invitees'])

    def test_team_detail_view_staff_user(self):
        test_data = {
            'teamId': self.team.public_id,
            'name': 'Sample Team1',
            'leader': 'sample_test_user1',
            'members': ['sample_test_user2'],
            'invitees': [],
            'events': [],
        }
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.force_login(user=self.staff_user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['teamId'], test_data['teamId'])
        self.assertEqual(response.data['name'], test_data['name'])
        self.assertEqual(response.data['leader'], test_data['leader'])
        self.assertEqual(response.data['members'], test_data['members'])
        self.assertEqual(response.data['invitees'], test_data['invitees'])

    def test_team_edit_view_unauthenticated(self):
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.login(user=None)  # self.client.logout()
        response = self.client.put(url,
                                   data=json.dumps({'name': 'New Team1'}),
                                   content_type='application/json'
                                   )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_team_edit_view_wrong_user(self):
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.force_login(user=self.user1)
        response = self.client.put(url,
                                   data=json.dumps({'name': 'New Team1'}),
                                   content_type='application/json'
                                   )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_team_edit_view_team_does_not_exist(self):
        url = reverse('team_details', args=('random_string',))
        self.client.force_login(user=self.user)
        response = self.client.put(url,
                                   data=json.dumps({'name': 'New Team1'}),
                                   content_type='application/json'
                                   )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_team_edit_view_no_name_input(self):
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.put(url,
                                   data=json.dumps({}),
                                   content_type='application/json'
                                   )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_team_edit_view_name_not_unique(self):
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.put(url,
                                   data=json.dumps({'name': 'Sample Team2'}),
                                   content_type='application/json'
                                   )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_team_edit_view(self):
        test_data = {
            'teamId': self.team.public_id,
            'name': 'New Team1',
            'leader': 'sample_test_user1',
            'members': ['sample_test_user2'],
            'invitees': [],
            'events': [],
        }
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.put(url,
                                   data=json.dumps({'name': 'New Team1'}),
                                   content_type='application/json'
                                   )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['teamId'], test_data['teamId'])
        self.assertEqual(response.data['name'], test_data['name'])
        self.assertEqual(response.data['leader'], test_data['leader'])
        self.assertEqual(response.data['members'], test_data['members'])
        self.assertEqual(response.data['invitees'], test_data['invitees'])

    def test_team_delete_view_unauthenticated(self):
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.login(user=None)  # self.client.logout()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_team_delete_view_wrong_user(self):
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.force_login(user=self.user1)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_team_delete_view_team_does_not_exist(self):
        url = reverse('team_details', args=('random_string',))
        self.client.force_login(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_team_delete_view_registered_team(self):
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_team_delete_view(self):
        self.registration.delete()
        url = reverse('team_details', args=(self.team.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamListCreateViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )
        self.user1 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user2',
                                         email='sampleuser2@test.com'
                                         )
        self.staff_user = User.objects.create(username='staff',
                                              first_name='staff',
                                              last_name='user',
                                              email='staff@test.com',
                                              is_staff=True
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
        self.team1 = Team.objects.create(team_leader=self.profile1,
                                         name='Sample Team2'
                                         )

        self.team_member1 = TeamMember.objects.create(team=self.team, profile=self.profile1,
                                                      invitation_accepted=True)
        self.team1_member1 = TeamMember.objects.create(team=self.team1, profile=self.profile)

        self.registration = TeamEventRegistration.objects.create(team=self.team, event=self.event,
                                                                 is_reserved=self.team.is_reserved
                                                                 )

    def test_team_create_view_unauthenticated(self):
        url = reverse('teams_list_create')
        self.client.login(user=None)
        response = self.client.post(url, json.dumps({'name': 'Sample Team3'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_team_create_view_no_name_input(self):
        url = reverse('teams_list_create')
        self.client.force_login(user=self.user)
        response = self.client.post(url, json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_team_create_view_name_not_unique(self):
        url = reverse('teams_list_create')
        self.client.force_login(user=self.user)
        response = self.client.post(url, json.dumps({'name': 'Sample Team1'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # TODO: def test_team_create_view_profile_not_complete(self):

    def test_team_create_view(self):
        url = reverse('teams_list_create')
        self.client.force_login(user=self.user)
        response = self.client.post(url, json.dumps({'name': 'Sample Team3'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Team.objects.filter(team_leader=self.profile, name='Sample Team3').exists())

    def test_team_list_view_unauthenticated(self):
        url = reverse('teams_list_create')
        self.client.login(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_team_list_view_user(self):
            url = reverse('teams_list_create')
            self.client.force_login(user=self.user)
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_team_list_view_staff_user(self):
            url = reverse('teams_list_create')
            self.client.force_login(user=self.staff_user)
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)



