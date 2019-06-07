from django.db import models
import datetime

# Create your models here.


class Volunteer(models.Model):
    name = models.CharField(max_length=40)
    task = models.CharField(max_length=40)
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=10, default='')
    profile_picture = models.CharField(max_length=200, default='profile_pictures/abstract_volunteer.jpg')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    rules = models.TextField(max_length=2000)
    fees = models.CharField(max_length=100)
    prerequisites = models.CharField(max_length=100)
    faq = models.TextField(max_length=2000)
    time = models.DateTimeField(default=datetime.datetime.now())
    venue = models.CharField(max_length=30)
    current_participants = models.ManyToManyField('events.Teams', related_name='events')
    max_participants = models.IntegerField()
    volunteer_list = models.ManyToManyField(Volunteer, related_name='events')

    def __str__(self):
        return self.name


class Teams(models.Model):
    team_name = models.CharField(max_length=30)
    members = models.ManyToManyField('registration.User', related_name='teams')


