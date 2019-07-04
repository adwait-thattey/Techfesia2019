from django.http import StreamingHttpResponse, HttpResponse
from .models import SoloEventRegistration, TeamEventRegistration, Team, TeamMember
from events.models import Event, TeamEvent
from .permissions import IsStaffUser
import csv
from itertools import chain
from rest_framework.decorators import permission_classes
from rest_framework.response import Response


class Echo:
    @staticmethod
    def write(value):
        return value


# @permission_classes([IsStaffUser,])  todo: Add Permission to make sure a staff user is accessing the data
def get_event_registrations(request, public_id):
    base_event = Event.objects.get(public_id=public_id)
    # if Event is a Team Event
    if base_event.team_event:
        try:
            event = base_event.teamevent
        except TeamEvent.DoesNotExist:
            return Response(status=404)
        header = (['Team Name', 'status', 'Reserved', 'Team Leader', 'Team Leader Email', 'college', 'registered on',
                   'All Members'],)
        data = ([
            i.team.name,
            i.status,
            str(i.is_reserved),
            i.team.team_leader.user.first_name + ' ' + i.team.team_leader.user.last_name,
            str(i.team.team_leader.user.email),
            i.team.team_leader.college.name,
            str(i.created_on),
            i.team.team_members
        ] for i in event.teameventregistration_set.all())
    else:
        event = base_event.soloevent
        header = (['Participant Name', 'status', 'Reserved', 'email', 'phone number', 'college', 'registered on'],)
        data = ([
            i.profile.user.first_name + ' ' + i.profile.user.last_name,
            i.status,
            str(i.is_reserved),
            str(i.profile.user.email),
            str(i.profile.phone_number),
            str(i.profile.college.name),
            str(i.created_on)
        ] for i in event.soloeventregistration_set.all())
    psuedo_buffer = Echo()
    writer = csv.writer(psuedo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in chain(header, data)), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + event.title + '-participants_list.csv"'
    response['status'] = 200
    return response


