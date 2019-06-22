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

    description = models.TextField(max_length=1000,
                                   null=True,
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

    participants_waiting_list = models.ManyToManyField(Team, related_name='waiting_list_events')

    max_participants = models.IntegerField(default=20)

    reserved_slots = models.IntegerField(default=0, help_text="No of participant slots reserved for external players")

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = generate_public_id(self)

        super().save(*args, **kwargs)


class SoloEvent(Event):
    pass


class TeamEvent(Event):
    min_team_size = models.IntegerField(default=1)
    max_team_size = models.IntegerField(default=1)
