from django.db import models
import datetime

# Create your models here.
from base.utils import generate_random_string, generate_public_id


class Team(models.Model):
    pass


class Category(models.Model):
    pass


class Tags(models.Model):
    pass


class Event(models.Model):
    public_id = models.CharField(max_length=100,
                                 unique=True,
                                 blank=True,
                                 db_index=True
                                 )

    title = models.CharField(max_length=100,
                             unique=True
                             )

    event_picture = models.URLField(null=True,
                                    blank=True
                                    )

    event_logo = models.URLField(null=True,
                                 blank=True
                                 )

    description = models.TextField(null=True,
                                   blank=True
                                   )

    start_date = models.DateField()

    start_time = models.TimeField()

    end_date = models.DateField()

    end_time = models.TimeField()

    venue = models.CharField(max_length=100,
                             default='to be determined'
                             )

    team_event = models.BooleanField(default=False)

    category = models.ManyToManyField(Category, related_name='events')

    tags = models.ManyToManyField(Tags, related_name='events')

    max_participants = models.IntegerField(default=20)

    reserved_slots = models.IntegerField(default=0, help_text="No of participant slots reserved for external players")

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = generate_public_id(self)

        super().save(*args, **kwargs)


class SoloEvent(Event):

    @property
    def event_type(self):
        return 'single'

    def current_participants(self):
        return self.soloeventregistration_set.filter(is_confirmed=True)

    def current_waiting_participants(self):
        return self.soloeventregistration_set.filter(is_complete=True, is_confirmed=False)

    def current_reserved_participants(self):
        return self.soloeventregistration_set.filter(is_confirmed=True, is_reserved=True)

    def current_waiting_reserved_participants(self):
        return self.soloeventregistration_set.filter(is_complete=True, is_confirmed=False, is_reserved=True)

    def refresh_participants(self):
        total_seats = self.max_participants
        total_reserved_seats = self.reserved_slots
        # If reserved registrations are available
        while self.current_waiting_reserved_participants().count() is not 0:
            # If reserved seats are available
            if self.current_reserved_participants().count() < total_reserved_seats:
                registration = self.current_waiting_reserved_participants().order_by('created_on')[0]
                registration.is_confirmed = True
                registration.save()
            else:
                break
        # If All Reserved Slots are full
        if self.current_reserved_participants().count() >= total_reserved_seats:
            while self.current_waiting_participants().count() is not 0:
                # Consider all registrations general
                if self.current_participants().count() < total_seats:
                    registration = self.current_waiting_participants().order_by('created_on')[0]
                    registration.is_confirmed = True
                    registration.save()
                else:
                    break
        else:
            while self.current_waiting_participants().count() is not 0:
                # Leave seats for Reserved Candidates
                if self.current_participants().filter(is_reserved=False).count() < total_seats - total_reserved_seats:
                    registration = self.current_waiting_participants().order_by('created_on')[0]
                    registration.is_confirmed = True
                    registration.save()
                else:
                    break


class TeamEvent(Event):
    min_team_size = models.IntegerField(default=1)
    max_team_size = models.IntegerField(default=1)

    @property
    def event_type(self):
        return 'team'

    def find_registration(self, user):
        if self.teameventregistration_set.filter(team__team_leader=user.profile).count() is 0:
            if self.teameventregistration_set.filter(team__teammember_set__profile=user.profile).count() is not 0:
                return self.teameventregistration_set.filter(team__teammember_set__profile=user.profile)[0]
            else:
                return None
        else:
            return self.teameventregistration_set.filter(team__team_leader__user=user)[0]

    def current_participants(self):
        return self.teameventregistration_set.filter(is_confirmed=True)

    def current_waiting_participants(self):
        return self.teameventregistration_set.filter(is_confirmed=False, is_complete=True)

    def current_reserved_participants(self):
        return self.teameventregistration_set.filter(is_confirmed=True, is_reserved=True)

    def current_waiting_reserved_participants(self):
        return self.teameventregistration_set.filter(is_confirmed=False, is_complete=True, is_reserved=True)

    def refresh_participants(self):
        total_seats = self.max_participants
        total_reserved_seats = self.reserved_slots

        reserved_slot = total_reserved_seats - self.current_reserved_participants().count()
        if reserved_slot > 0:
            for registration in self.current_waiting_reserved_participants().order_by('created_on')[:reserved_slot]:
                registration.is_confirmed = True
                registration.save()

        if self.current_reserved_participants().count() < total_reserved_seats:
            reserved_slot = total_seats - total_reserved_seats - self.current_participants().filter(is_reserved=False)
        else:
            reserved_slot = total_seats - self.current_participants().count()
        for registration in self.current_waiting_participants().order_by('created_on')[:reserved_slot]:
            registration.is_confirmed = True
            registration.save()
