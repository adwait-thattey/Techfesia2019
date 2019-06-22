from django.db import models
import datetime

# Create your models here.
from base.utils import generate_random_string


class Team(models.Model):
    pass


class Category(models.Model):
    pass


class Tags(models.Model):
    pass


class Event(models.Model):
    public_id = models.CharField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=100, unique=True)
    event_picture = models.URLField()
    event_logo = models.URLField()
    description = models.CharField(max_length=1000)
    # description = models.JsonField()
    date = models.DateField(default=datetime.date(2000, 1, 1))
    time = models.TimeField(default=datetime.time(12, 0, 0))
    venue = models.CharField(max_length=100)
    min_team_size = models.IntegerField(default=1)
    max_team_size = models.IntegerField(default=1)
    participants = models.ManyToManyField(Team, related_name='participated_events')
    category = models.ManyToManyField(Category, related_name='events')
    tags = models.ManyToManyField(Tags, related_name='events')
    min_participants = models.IntegerField()
    max_participants = models.IntegerField()
    participants_waiting_list = models.ManyToManyField(Team, related_name='waiting_list_events')

    def is_single_event(self):
        return self.max_participants == 1

    @property
    def current_participants(self):
        return self.participants.count()

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = generate_random_string()

        super().save(*args, **kwargs)

