from registration.models import User
from accounts.models import Profile, Institute
from tickets.models import Ticket, TicketComment
from events.models import TeamEvent, Event
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import datetime as dt
import json


class TicketCreateListViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )
        self.user1 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user1',
                                         email='sampleuser2@test.com'
                                         )
        self.staff_user = User.objects.create(username='staff',
                                              first_name='staff',
                                              last_name='user',
                                              email='staff_user@test.com',
                                              is_staff=True
                                              )
        self.institute = Institute.objects.create()
        self.event = TeamEvent.objects.create(title='Sample Solo Event',
                                              start_date=dt.date(2019, 7, 1),
                                              end_date=dt.date(2019, 7, 1),
                                              start_time=dt.time(12, 0, 0),
                                              end_time=dt.time(15, 0, 0),
                                              max_team_size=4,
                                              min_team_size=2
                                              )

        self.profile = Profile.objects.create(user=self.user,
                                              college=self.institute,
                                              phone_number='+991234567890'
                                              )
        self.profile1 = Profile.objects.create(user=self.user1,
                                               college=self.institute,
                                               phone_number='+991234567891'
                                               )

        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile,
                                            )

    def test_ticket_list_view_unauthenticated(self):
        url = reverse('ticket_list', args=(self.user.username,))
        self.client.login(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ticket_list_view_wrong_user(self):
        url = reverse('ticket_list', args=(self.user1.username,))
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_ticket_list_view_staff_user(self):
        url = reverse('tickets_list_staff_create_user')
        self.client.force_login(user=self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_list_view_staff_user_filter_by_user(self):
        url = reverse('tickets_list_staff_create_user')
        self.client.force_login(user=self.staff_user)
        response = self.client.get(url, {'user': self.user.username})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_list_view_staff_user_filter_by_status(self):
        url = reverse('tickets_list_staff_create_user')
        self.client.force_login(user=self.staff_user)
        response = self.client.get(url, {'status': 'Opened'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_list_view_staff_user_filter_by_event(self):
        url = reverse('tickets_list_staff_create_user')
        self.client.force_login(user=self.staff_user)
        response = self.client.get(url, {'event': self.event.public_id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_list_view(self):
        url = reverse('ticket_list', args=(self.user.username,))
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_list_view_with_username(self):
        url = reverse('ticket_list', args=(self.user.username,))
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_create_view_unauthenticated(self):
        url = reverse('tickets_list_staff_create_user')
        self.client.login(user=None)
        response = self.client.post(url, data={'title': 'Sample Ticket3', 'description': 'sample ticket description'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ticket_create_view_missing_parameters(self):
        url = reverse('tickets_list_staff_create_user')
        self.client.force_login(user=self.user)
        response = self.client.post(url, json.dumps({'title': 'Sample Ticket3'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(url, json.dumps({'description': 'sample data'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_ticket_create_view(self):
        url = reverse('tickets_list_staff_create_user')
        self.client.force_login(user=self.user)
        response = self.client.post(url,
                                    json.dumps({'title': 'Sample Ticket3',
                                                'view': 'private',
                                                'description': 'sample ticket description'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Ticket.objects.filter(opened_by=self.profile))


class TicketDetailViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )
        self.user1 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user1',
                                         email='sampleuser2@test.com'
                                         )
        self.staff_user = User.objects.create(username='staff',
                                              first_name='staff',
                                              last_name='user',
                                              email='staff_user@test.com',
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

        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile,
                                            is_public=False
                                            )

    def test_ticket_detail_view_unauthorised(self):
        url = reverse('ticket_detail', args=(self.ticket.public_id,))
        self.client.login(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ticket_detail_wrong_user(self):
        url = reverse('ticket_detail', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_ticket_detail_view_staff_user(self):
        url = reverse('ticket_detail', args=(self.ticket.public_id,))
        self.client.force_login(user=self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_detail_view(self):
        url = reverse('ticket_detail', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PublicTicketListViewTestCase(APITestCase):
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
        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile,
                                            is_public=False
                                            )

    def test_public_ticket_list_view(self):
        url = reverse('tickets_list_public')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TicketCloseViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )
        self.staff_user = User.objects.create(username='staff',
                                              first_name='staff',
                                              last_name='user',
                                              email='staff_user@test.com',
                                              is_staff=True
                                              )

        self.institute = Institute.objects.create()

        self.profile = Profile.objects.create(user=self.user,
                                              college=self.institute,
                                              phone_number='+991234567890'
                                              )
        self.staff_profile = Profile.objects.create(user=self.staff_user,
                                                    college=self.institute,
                                                    phone_number='+991234567899'
                                                    )
        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile,
                                            is_public=False
                                            )

    def test_ticket_close_view_unauthenticated(self):
        url = reverse('ticket_close', args=(self.ticket.public_id,))
        self.client.login(user=None)
        response = self.client.put(url, data={'content': 'sample content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ticket_close_view_wrong_user(self):
        url = reverse('ticket_close', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.put(url, data={'content': 'sample content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_ticket_close_view_no_content(self):
        url = reverse('ticket_close', args=(self.ticket.public_id,))
        self.client.force_login(user=self.staff_user)
        response = self.client.put(url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_ticket_close_view_does_not_exist(self):
        url = reverse('ticket_close', args=('random_string',))
        self.client.force_login(user=self.staff_user)
        response = self.client.put(url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ticket_close_view_already_closed(self):
        self.ticket.status = 'Solved'
        self.ticket.save()
        url = reverse('ticket_close', args=(self.ticket.public_id,))
        self.client.force_login(user=self.staff_user)
        response = self.client.put(url, data={'content': 'sample content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_ticket_close_view(self):
        url = reverse('ticket_close', args=(self.ticket.public_id,))
        self.client.force_login(user=self.staff_user)
        response = self.client.put(url, data={'content': 'sample content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TicketCommentListCreateViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )

        self.user1 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user1',
                                         email='sampleuser2@test.com'
                                         )
        self.user2 = User.objects.create(username='sample_test_user3',
                                         first_name='sample',
                                         last_name='user2',
                                         email='sampleuser3@test.com'
                                         )
        self.staff_user = User.objects.create(username='staff',
                                              first_name='staff',
                                              last_name='user',
                                              email='staffuser@test.com',
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
        self.staff_profile = Profile.objects.create(user=self.staff_user,
                                                    college=self.institute,
                                                    phone_number='+991234567899'
                                                    )
        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile
                                            )
        self.ticket1 = Ticket.objects.create(title='Sample Ticket2',
                                             description='Some sample description',
                                             opened_by=self.profile1,
                                             is_public=False,
                                             )

        self.ticket_comment = TicketComment.objects.create(ticket=self.ticket,
                                                           commenter=self.profile1,
                                                           text='Comment Text'
                                                           )

        self.ticket_comment1 = TicketComment.objects.create(ticket=self.ticket,
                                                            commenter=self.profile,
                                                            text='Comment Text 2'
                                                            )

    def test_ticket_comment_list_view_unauthenticated(self):
        url = reverse('ticket_comment_create_list', args=(self.ticket.public_id,))
        self.client.login(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ticket_comment_list_view_wrong_user(self):
        url = reverse('ticket_comment_create_list', args=(self.ticket1.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_ticket_comment_list_view_does_not_exist(self):
        url = reverse('ticket_comment_create_list', args=('random_string',))
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ticket_comment_list_view(self):
        url = reverse('ticket_comment_create_list', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_comment_create_view_unauthenticated(self):
        url = reverse('ticket_comment_create_list', args=(self.ticket.public_id,))
        self.client.login(user=None)
        response = self.client.post(url, json.dumps({'text': 'ticket comment 1'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ticket_comment_create_view_no_input(self):
        url = reverse('ticket_comment_create_list', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user1)
        response = self.client.post(url, json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_ticket_comment_create_view_ticket_does_not_exist(self):
        url = reverse('ticket_comment_create_list', args=('random_string',))
        self.client.force_login(user=self.user1)
        response = self.client.post(url, json.dumps({'text': 'ticket comment 1'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ticket_comment_create_view_profile_not_complete(self):
        url = reverse('ticket_comment_create_list', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user2)
        response = self.client.post(url, json.dumps({'text': 'ticket comment 1'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_ticket_comment_create_view(self):
        url = reverse('ticket_comment_create_list', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user1)
        response = self.client.post(url, json.dumps({'text': 'ticket comment 1'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_ticket_comment_create_view_staff(self):
        url = reverse('ticket_comment_create_list', args=(self.ticket1.public_id,))
        self.client.force_login(user=self.staff_user)
        response = self.client.post(url, json.dumps({'text': 'ticket comment 1'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TicketCommentDetailUpdateDeleteView(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )

        self.user1 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user1',
                                         email='sampleuser2@test.com'
                                         )
        self.staff_user = User.objects.create(username='staff',
                                              first_name='staff',
                                              last_name='user',
                                              email='staffuser@test.com',
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
        self.staff_profile = Profile.objects.create(user=self.staff_user,
                                                    college=self.institute,
                                                    phone_number='+991234567899'
                                                    )
        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile
                                            )
        self.ticket1 = Ticket.objects.create(title='Sample Ticket2',
                                             description='Some sample description',
                                             opened_by=self.profile1,
                                             is_public=False,
                                             )

        self.ticket_comment = TicketComment.objects.create(ticket=self.ticket,
                                                           commenter=self.profile1,
                                                           text='Comment Text'
                                                           )

        self.ticket1_comment = TicketComment.objects.create(ticket=self.ticket1,
                                                            commenter=self.profile,
                                                            text='Comment Text 2'
                                                            )

    def test_ticket_comment_detail_view_unauthenticated(self):
        url = reverse('ticket_comment_detail', args=(self.ticket1.public_id, self.ticket1_comment.public_id,))
        self.client.login(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ticket_comment_detail_view_ticket_does_not_exist(self):
        url = reverse('ticket_comment_detail', args=('random_string', self.ticket_comment.public_id,))
        self.client.force_login(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ticket_comment_detail_view_comment_does_not_exist(self):
        url = reverse('ticket_comment_detail', args=(self.ticket.public_id, 'random_string',))
        self.client.login(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ticket_comment_detail_view_public(self):
        url = reverse('ticket_comment_detail', args=(self.ticket.public_id, self.ticket_comment.public_id,))
        self.client.login(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_comment_detail_view_staff_private(self):
        url = reverse('ticket_comment_detail', args=(self.ticket1.public_id, self.ticket1_comment.public_id,))
        self.client.force_login(user=self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_comment_detail_view_staff(self):
        url = reverse('ticket_comment_detail', args=(self.ticket.public_id, self.ticket_comment.public_id,))
        self.client.force_login(user=self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_comment_detail_view(self):
        url = reverse('ticket_comment_detail', args=(self.ticket.public_id, self.ticket_comment.public_id,))
        self.client.force_login(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_comment_delete_view_unauthenticated(self):
        url = reverse('ticket_comment_detail', args=(self.ticket.public_id, self.ticket_comment.public_id,))
        self.client.login(user=None)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ticket_comment_delete_view_does_not_exist(self):
        url = reverse('ticket_comment_detail', args=(self.ticket.public_id, 'random_string',))
        self.client.force_login(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        url = reverse('ticket_comment_detail', args=('random_string', self.ticket_comment.public_id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_ticket_comment_delete_view(self):
        url = reverse('ticket_comment_detail', args=(self.ticket.public_id, self.ticket_comment.public_id,))
        public_id = self.ticket_comment.public_id
        self.client.force_login(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(TicketComment.objects.filter(public_id=public_id).exists())

    def test_ticket_comment_update_view_unauthenticated(self):
        url = reverse('ticket_comment_detail', args=(self.ticket.public_id, self.ticket_comment.public_id,))
        self.client.login(user=None)
        response = self.client.put(url, json.dumps({'text': 'Updated comment'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ticket_comment_update_view_does_not_exist(self):
        url = reverse('ticket_comment_detail', args=(self.ticket.public_id, 'random_string',))
        self.client.force_login(user=self.user)
        response = self.client.put(url, json.dumps({'text': 'Updated comment'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        url = reverse('ticket_comment_detail', args=('random_string', self.ticket_comment.public_id,))
        response = self.client.put(url, json.dumps({'text': 'Updated comment'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_ticket_comment_update_view_no_input(self):
        url = reverse('ticket_comment_detail', args=(self.ticket.public_id, self.ticket_comment.public_id,))
        public_id = self.ticket_comment.public_id
        self.client.force_login(user=self.user)
        response = self.client.put(url, json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_ticket_comment_update_view(self):
        url = reverse('ticket_comment_detail', args=(self.ticket.public_id, self.ticket_comment.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.put(url, json.dumps({'text': 'Updated comment'}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ticket_comment.refresh_from_db()
        self.assertEqual(self.ticket_comment.text, 'Updated comment')


class TicketSubscribeViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )
        self.user1 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user1',
                                         email='sampleuser2@test.com'
                                         )
        self.user2 = User.objects.create(username='sample_test_user3',
                                         first_name='sample',
                                         last_name='user2',
                                         email='sampleuser3@test.com'
                                         )
        self.staff_user = User.objects.create(username='staff',
                                              first_name='staff',
                                              last_name='user',
                                              email='staff_user@test.com',
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

        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile
                                            )
        self.ticket1 = Ticket.objects.create(title='Sample Ticket2',
                                             description='Some sample description',
                                             opened_by=self.profile1,
                                             is_public=False
                                             )

    def test_ticket_subscribe_view_unauthenticated(self):
        url = reverse('ticket_subscribe', args=(self.ticket.public_id,))
        self.client.login(user=None)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ticket_subscribe_view_does_not_exist(self):
        url = reverse('ticket_subscribe', args=('random_string',))
        self.client.force_login(user=self.user1)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ticket_subscribe_view_profile_not_complete(self):
        url = reverse('ticket_subscribe', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user2)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_ticket_subscribe_view_ticket_private(self):
        url = reverse('ticket_subscribe', args=(self.ticket1.public_id,))
        self.client.force_login(user=self.user)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_ticket_subscribe_view(self):
        url = reverse('ticket_subscribe', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user1)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ticket.refresh_from_db()
        self.assertTrue(self.ticket.subscribers.filter(user=self.user1).exists())


class TicketUnsubscribeViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )
        self.user1 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user1',
                                         email='sampleuser2@test.com'
                                         )
        self.user2 = User.objects.create(username='sample_test_user3',
                                         first_name='sample',
                                         last_name='user2',
                                         email='sampleuser3@test.com'
                                         )
        self.staff_user = User.objects.create(username='staff',
                                              first_name='staff',
                                              last_name='user',
                                              email='staff_user@test.com',
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
        self.profile2 = Profile.objects.create(user=self.user2,
                                               college=self.institute,
                                               phone_number='+991234567892'
                                               )

        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile
                                            )

        self.ticket.subscribers.add(self.profile1)

    def test_ticket_unsubscribe_view_unauthenticated(self):
        url = reverse('ticket_unsubscribe', args=(self.ticket.public_id,))
        self.client.login(user=None)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ticket_unsubscribe_view_does_not_exist(self):
        url = reverse('ticket_unsubscribe', args=('random_string',))
        self.client.force_login(user=self.user1)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ticket_unsubscribe_view_profile_not_complete(self):
        url = reverse('ticket_unsubscribe', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user2)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_ticket_unsubscribe_view_not_subscribed(self):
        url = reverse('ticket_unsubscribe', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user2)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_ticket_unsubscribe_view(self):
        url = reverse('ticket_unsubscribe', args=(self.ticket.public_id,))
        self.client.force_login(user=self.user1)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ticket.refresh_from_db()
        self.assertFalse(self.ticket.subscribers.filter(user=self.user1).exists())

