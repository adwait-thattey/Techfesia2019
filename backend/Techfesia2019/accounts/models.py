from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from events.models import Event
from registration.models import User


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    profile_pic = models.URLField()
    phone_number = models.CharField(max_length=13, validators=[MinLengthValidator(13)])
    college_name = models.CharField(max_length=150)


class ProfileOrganizer(Profile):
    events = models.ManyToManyField(to=Event, related_name="organizers")


class ProfileVolunteer(Profile):
    events = models.ManyToManyField(to=Event, related_name="volunteers")
