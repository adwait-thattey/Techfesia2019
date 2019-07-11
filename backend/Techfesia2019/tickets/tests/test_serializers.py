from django.test import TestCase
from tickets.models import Ticket, TicketComment
from tickets.serializers import TicketSerializer, TicketCommentSerializer
from registration.models import User
from accounts.models import Profile, Institute
import datetime as dt


class TicketSerializerTestCase(TestCase):
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

        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile,
                                            )
        self.test_data = {
            'publicId': self.ticket.public_id,
            'title': 'Sample Ticket1',
            'description': 'Some sample description',
            'openedBy': 'sample_test_user1',
            'openingDate': dt.date.today().strftime('%Y-%m-%d'),
            'status': 'Opened',
            'event': None,
            'solvedBy': None,
            'solvingDate': None,
            'content': '',
            'subscribers': []
        }
        self.serializer = TicketSerializer(instance=self.ticket)

    def test_contain_all_fields(self):
        self.assertCountEqual(set(self.test_data.keys()), set(self.serializer.data.keys()))

    def test_public_id(self):
        self.assertEqual(self.test_data['publicId'], self.serializer['publicId'].value)

    def test_title(self):
        self.assertEqual(self.test_data['title'], self.serializer['title'].value)

    def test_description(self):
        self.assertEqual(self.test_data['description'], self.serializer['description'].value)

    def test_opened_by(self):
        self.assertEqual(self.test_data['openedBy'], self.serializer['openedBy'].value)

    def test_opening_date(self):
        self.assertEqual(self.test_data['openingDate'], self.serializer['openingDate'].value)

    def test_status(self):
        self.assertEqual(self.test_data['status'], self.serializer['status'].value)

    def test_event(self):
        self.assertEqual(self.test_data['event'], self.serializer['event'].value)

    def test_solved_by(self):
        self.assertEqual(self.test_data['solvedBy'], self.serializer['solvedBy'].value)

    def test_solving_date(self):
        self.assertEqual(self.test_data['solvingDate'], self.serializer['solvingDate'].value)

    def test_content(self):
        self.assertEqual(self.test_data['content'], self.serializer['content'].value)

    def test_subscribers(self):
        self.assertEqual(self.test_data['subscribers'], self.serializer['subscribers'].value)


class TicketCommentSerializerTestCase(TestCase):
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

        self.profile = Profile.objects.get(user=self.user)
        self.profile.college = self.institute
        self.profile.save()
        self.profile1 = Profile.objects.get(user=self.user1)
        self.profile1.college = self.institute
        self.profile1.save()

        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile
                                            )

        self.ticket_comment = TicketComment.objects.create(ticket=self.ticket,
                                                           commenter=self.profile1,
                                                           text='Comment Text')

        self.serializer = TicketCommentSerializer(instance=self.ticket_comment)

        self.test_data = {
            'publicId': self.ticket_comment.public_id,
            'ticket': self.ticket.public_id,
            'commenter': 'sample_test_user2',
            'text': 'Comment Text',
            'postingDate': self.ticket_comment.posting_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        }

    def test_contain_all_fields(self):
        self.assertCountEqual(set(self.serializer.data.keys()), set(self.test_data.keys()))

    def test_public_id(self):
        self.assertEqual(self.test_data['publicId'], self.serializer['publicId'].value)

    def test_ticket(self):
        self.assertEqual(self.test_data['ticket'], self.serializer['ticket'].value)

    def test_commenter(self):
        self.assertEqual(self.test_data['commenter'], self.serializer['commenter'].value)

    def test_text(self):
        self.assertEqual(self.test_data['text'], self.serializer['text'].value)

    def test_posting_date(self):
        self.assertEqual(self.test_data['postingDate'], self.serializer['postingDate'].value)

