import datetime as dt
from json import dumps as json_dumps
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from registration.models import User
from events.models import SoloEvent
from event_registrations.models import SoloEventRegistration
from payments.models import Transaction


class PaymentInitiateViewTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='test_user1',
                                         first_name='test', last_name='user',
                                         email='test_user1@test.com', email_confirmed=True
                                         )

        self.user2 = User.objects.create(username='test_user2',
                                         first_name='test', last_name='user',
                                         email='test_user2@test.com', email_confirmed=True
                                         )

        self.profile1 = self.user1.profile
        self.profile2 = self.user2.profile

        self.event1 = SoloEvent.objects.create(title='SoloEvent1',
                                               start_date=dt.date(2019, 7, 19), end_date=dt.date(2019, 7, 19),
                                               start_time=dt.time(12, 0, 0),  end_time=dt.time(15, 0, 0),
                                               fee=100, reserved_fee=80, reserved_slots=10, max_participants=20
                                               )

        self.event2 = SoloEvent.objects.create(title='SoloEvent2',
                                               start_date=dt.date(2019, 7, 19), end_date=dt.date(2019, 7, 19),
                                               start_time=dt.time(12, 0, 0),  end_time=dt.time(15, 0, 0),
                                               fee=100, reserved_fee=0, reserved_slots=10, max_participants=20
                                               )

        self.registration1 = SoloEventRegistration.objects.create(event=self.event1, profile=self.profile1)

        self.registration2 = SoloEventRegistration.objects.create(event=self.event1, profile=self.profile2,
                                                                  is_reserved=True)

        self.registration3 = SoloEventRegistration.objects.create(event=self.event2, profile=self.profile2,
                                                                  is_reserved=True, is_complete=True)

        self.registration3_transaction = Transaction.objects.create(created_by=self.profile1,
                                                                    solo_registration=self.registration1,
                                                                    status='Failed')

        self.registration3_transaction = Transaction.objects.create(created_by=self.profile2,
                                                                    solo_registration=self.registration3,
                                                                    status='Successful')

    def test_payment_initiate_view_unauthenticated(self):
        url = reverse('payment_initiate')
        self.client.login(user=None)
        response = self.client.post(url,
                                    data=json_dumps({'eventPublicId': self.event1.public_id,
                                                     'registrationId': self.registration1.public_id}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_payment_initiate_view_wrong_user(self):
        url = reverse('payment_initiate')
        self.client.force_login(user=self.user2)
        response = self.client.post(url,
                                    data=json_dumps({'eventPublicId': self.event1.public_id,
                                                     'registrationId': self.registration1.public_id}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_payment_initiate_view_invalid_data(self):
        url = reverse('payment_initiate')
        self.client.force_login(user=self.user1)
        response = self.client.post(url,
                                    data=json_dumps({'eventPublicId': 'random_string',
                                                     'registrationId': self.registration1.public_id}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.post(url,
                                    data=json_dumps({'eventPublicId': self.event1.public_id,
                                                     'registrationId': 'random_string'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_payment_initiate_view_missing_data(self):
        url = reverse('payment_initiate')
        self.client.force_login(user=self.user1)
        response = self.client.post(url,
                                    data=json_dumps({'eventPublicId': self.event1.public_id}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        response = self.client.post(url,
                                    data=json_dumps({'registrationId': self.registration1.public_id}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_payment_initiate_view_already_paid(self):
        url = reverse('payment_initiate')
        self.client.force_login(user=self.user2)
        response = self.client.post(url,
                                    data=json_dumps({'eventPublicId': self.event2.public_id,
                                                     'registrationId': self.registration3.public_id}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_payment_initiate_view_again(self):
        url = reverse('payment_initiate')
        self.client.force_login(user=self.user2)
        response = self.client.post(url,
                                    data=json_dumps({'eventPublicId': self.event1.public_id,
                                                     'registrationId': self.registration2.public_id}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.content_type, 'text/html')

    def test_payment_initiate_view(self):
        url = reverse('payment_initiate')
        self.client.force_login(user=self.user1)
        response = self.client.post(url,
                                    data=json_dumps({'eventPublicId': self.event1.public_id,
                                                     'registrationId': self.registration1.public_id}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.content_type, 'text/html')


