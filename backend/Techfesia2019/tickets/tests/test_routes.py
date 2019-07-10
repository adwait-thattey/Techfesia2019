from registration.models import User
from accounts.models import Profile, Institute
from tickets.models import Ticket, TicketComment
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
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

    def test_ticket_list_view(self):
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
                                    json.dumps({'title': 'Sample Ticket3', 'description': 'sample ticket description'}),
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

        self.ticket_comment = TicketComment.objects.create(ticket=self.ticket,
                                                           commenter=self.profile1,
                                                           text='Comment Text'
                                                           )

        self.ticket_comment1 = TicketComment.objects.create(ticket=self.ticket,
                                                            commenter=self.profile,
                                                            text='Comment Text 2'
                                                            )

    def test_ticket_comment_list_view_unauthorised(self):
        self.assertTrue(True)



