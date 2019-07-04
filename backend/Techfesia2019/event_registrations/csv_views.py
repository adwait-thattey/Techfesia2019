from django.http import StreamingHttpResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from events.models import Event, TeamEvent
from .permissions import IsStaffUser
from .forms import StaffLoginForm
import csv
from itertools import chain
from rest_framework.decorators import permission_classes
from rest_framework.response import Response


class Echo:
    @staticmethod
    def write(value):
        return value


@login_required(login_url='staff_login', redirect_field_name='next')
@permission_classes([IsStaffUser, ])  # todo: Add Permission to make sure a staff user is accessing the data
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


def staff_login(request):
    if request.method == 'POST':
        print(request.POST)
        try:
            next_url = request.POST['next']
        except KeyError:
            next_url = None
        print(next_url)
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if next_url:
                    print(next_url)
                    return HttpResponseRedirect(next_url)
                else:
                    return HttpResponse('Login Successful')
            else:
                context = {'form': form, 'error': 'User does not exist'}
                return render(request, 'event_registrations/staff_login.html', context=context)
        else:
            context = {'form': form, 'error': 'Unable to process, Please Try Again'}
            return render(request, 'event_registrations/staff_login.html', context=context)
    elif request.method == 'GET':
        context = {'form': StaffLoginForm()}
        if dict(request.GET).get('next'):
            next_url = request.GET['next']
            context['next'] = next_url
        return render(request, 'event_registrations/staff_login.html', context=context)
