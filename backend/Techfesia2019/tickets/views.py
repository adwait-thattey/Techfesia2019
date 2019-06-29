from .models import Ticket, TicketComment
from .permissions import IsStaffUserOrOwnerOrPost
from .serializers import TicketSerializer#, TicketCommentSerializer
from accounts.models import Profile
from registration.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.


class TicketCreateListView(APIView):
    permission_classes = (IsStaffUserOrOwnerOrPost,)

    def get(self, request, format=None):
        tickets = Ticket.objects.all()
        if not request.user.is_staff:
            profile = Profile.objects.get(user=request.user)
            tickets = tickets.filter(opened_by=profile)
        q_status, q_user, q_event = request.GET.get('status'), request.GET.get('user'), request.GET.get('event')
        if q_user and request.user.is_staff:
            tickets = tickets.filter(opened_by=Profile.objects.get(user=User.objects.get(username=q_user)))
        if q_status:
            tickets = tickets.filter(status=q_status)
        if q_event:
            tickets = tickets.filter(event__public_id=q_event)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'message': 'Wrong data'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

