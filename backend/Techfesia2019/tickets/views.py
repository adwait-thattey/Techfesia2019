import datetime as dt
from .models import Ticket, TicketComment
from .permissions import IsStaffUser, IsAuthenticatedOrGet
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from .serializers import TicketSerializer, TicketCommentSerializer
from events.models import Event
from accounts.models import Profile
from registration.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.dispatch import Signal, receiver
from django.core.mail import send_mail
from django.template.loader import get_template
# Create your views here.


notifications = Signal(providing_args = ['subject','id'])

class TicketCreateListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username=None, format=None):
        tickets = Ticket.objects.all()
        if request.user.is_staff:
            if username:
                tickets = tickets.filter(opened_by__user__username=username)
            q_status, q_user, q_event = request.GET.get('status'), request.GET.get('user'), request.GET.get('event')
            if q_user and request.user.is_staff:
                tickets = tickets.filter(opened_by=Profile.objects.get(user=User.objects.get(username=q_user)))
            if q_status:
                tickets = tickets.filter(status=q_status)
            if q_event:
                tickets = tickets.filter(event__public_id=q_event)
        else:
            if username == request.user.username:
                profile = Profile.objects.get(user=request.user)
                tickets = tickets.filter(opened_by=profile)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = dict(JSONParser().parse(request))
        ticket = Ticket()
        ticket.opened_by = request.user.profile
        try:
            ticket.title = data['title']
            ticket.description = data['description']
        except KeyError as key:
            return Response({'error': 'Missing data ' + str(key)}, status=status.HTTP_400_BAD_REQUEST)
        if data.get('view') == 'private':
            ticket.is_public = False
        if data.get('event'):
            ticket.event = Event.objects.get(public_id=data.get('event'))
        ticket.save()
        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TicketDetailView(APIView):
    def get(self, request, public_id, format=None):
        try:
            ticket = Ticket.objects.get(public_id=public_id)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if ticket.is_public or ticket.opened_by.user == request.user or request.user.is_staff:
            serializer = TicketSerializer(ticket)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if str(request.user) == 'AnonymousUser':
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            return Response(status=status.HTTP_403_FORBIDDEN)


class TicketCloseView(APIView):
    permission_classes = (IsStaffUser,)

    def put(self, request, public_id, format=None):
        try:
            ticket = Ticket.objects.get(public_id=public_id)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if ticket.status == 'Solved':
            return Response({'error': 'Ticket is already Closed/Solved'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            ticket.solved_by = request.user.profile
            ticket.solving_date = dt.date.today()
            ticket.status = 'Solved'
            ticket.content = dict(request.data).get('content')
            try:
                ticket.save()
                notifications.send(
                    sender = Ticket,
                    ticket_id = ticket.public_id 
                    )
            except IntegrityError:
                return Response({'error': 'required field "content" not provided'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PublicTicketListView(APIView):
    # permission_classes = ()
    # TODO: Check if Authentication is required to view Public Tickets
    def get(self, request, format=None):
        tickets = Ticket.objects.filter(is_public=True)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TicketCommentListCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, public_id, format=None):
        try:
            ticket = Ticket.objects.get(public_id=public_id)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if ticket.is_public or request.user.is_staff or request.user.profile is ticket.opened_by:
            comments = TicketComment.objects.filter(ticket=ticket)
            serializer = TicketCommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def post(self, request, public_id, format=None):
        data = JSONParser().parse(request)
        comment = TicketComment()
        try:
            comment.text = data['text']
            comment.ticket = Ticket.objects.get(public_id=public_id)
            comment.commenter = request.user.profile
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket Doesn\'t Exist'}, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response({'error': 'Missing data'}, status=status.HTTP_400_BAD_REQUEST)
        comment.save()
        notifications.send(
            sender = TicketComment,
            id = comment.public_id,
            )
        serializer = TicketCommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TicketCommentDetailUpdateDeleteView(APIView):
    permission_classes = (IsAuthenticatedOrGet,)

    def get(self, request, public_id, comment_id, format=None):
        try:
            ticket = Ticket.objects.get(public_id=public_id)
            comment = TicketComment.objects.get(public_id=comment_id)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket Not Found'}, status=status.HTTP_404_NOT_FOUND)
        except TicketComment.DoesNotExist:
            return Response({'error': 'Comment Not Found'}, status=status.HTTP_404_NOT_FOUND)
        if not ticket.is_public:
            if str(request.user) == 'AnonymousUser':
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            elif request.user.profile == ticket.opened_by or request.user.is_staff:
                serializer = TicketCommentSerializer(comment)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = TicketCommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, public_id, comment_id, format=None):
        data = JSONParser().parse(request)
        try:
            ticket = Ticket.objects.get(public_id=public_id)
            comment = TicketComment.objects.get(public_id=comment_id)
            text = data['text']
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket Not Found'}, status=status.HTTP_204_NO_CONTENT)
        except TicketComment.DoesNotExist:
            return Response({'error': 'Comment Not Found'}, status=status.HTTP_204_NO_CONTENT)
        except KeyError:
            return Response({'error': 'text not provided'}, status=status.HTTP_400_BAD_REQUEST)
        if ticket.opened_by.user == request.user:
            comment.text = text
            comment.save()
            serializer = TicketCommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, public_id, comment_id, format=None):
        try:
            comment = TicketComment.objects.get(public_id=comment_id, ticket__public_id=public_id)
        except TicketComment.DoesNotExist:
            return Response({'error': 'Comment Not Found'}, status=status.HTTP_204_NO_CONTENT)
        comment.delete()
        return Response({'message': 'Comment Deleted'}, status=status.HTTP_200_OK)


class TicketSubscribeView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, public_id, format=None):
        try:
            ticket = Ticket.objects.get(public_id=public_id)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if not ticket.is_public:
            return Response(status=status.HTTP_403_FORBIDDEN)
        profile = Profile.objects.get(user=request.user)
        ticket.subscribers.add(profile)
        ticket.save()
        return Response({'message': 'subscribed to ticket'}, status=status.HTTP_200_OK)


class TicketUnsubscribeView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, public_id, format=None):
        try:
            ticket = Ticket.objects.get(public_id=public_id)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if not ticket.is_public:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if not ticket.subscribers.filter(user=request.user).exists():
            return Response({'error': 'You are not subscribed to this ticket'},
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY
                            )
        profile = Profile.objects.get(user=request.user)
        ticket.subscribers.remove(profile)
        ticket.save()
        return Response({'message': 'unsubscribed from ticket'}, status=status.HTTP_200_OK)

@receiver(notifications)
def send_emails(sender, **kwargs):
    if(sender == Ticket):
        ticket_id = kwargs['id']
        ticket = Ticket.objects.filter(public_id = ticket_id)
        context = {
            'ticket' : ticket,
            'message': `Ticket has been closed by {}`.format(ticket.solved_by.username)
        }
        subject = `Ticket no.{} is solved`.format(ticket_id)

    else:
        comment_id = kwargs['id']
        comment = TicketComment.objects.filter(public_id = comment_id)
        context = {
            'ticket' : comment.ticket,
            'message': `A new comment has been posted by {}`.format(comment.commenter.username)
        }
    
    message = get_template('base.html').render(context)
    send_mail(subject, message,from_email,to_email,fail_silently = false)
    