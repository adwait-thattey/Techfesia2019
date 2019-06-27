from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from events.models import Event, SoloEvent
from registration.models import User


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    profile_pic = models.URLField()
    phone_number = models.CharField(max_length=13, validators=[MinLengthValidator(13)])
    college_name = models.CharField(max_length=150)

    @property
    def get_user_username(self):
        return self.user.username


class ProfileParticipant(models.Model):
    profile = models.OneToOneField(to=Profile, on_delete=models.CASCADE)


class ProfileOrganizer(models.Model):
    profile = models.OneToOneField(to=Profile, on_delete=models.CASCADE)
    events = models.ManyToManyField(to=Event, related_name="organizers")


class ProfileVolunteer(models.Model):
    profile = models.OneToOneField(to=Profile, on_delete=models.CASCADE)
    events = models.ManyToManyField(to=Event, related_name="volunteers")
