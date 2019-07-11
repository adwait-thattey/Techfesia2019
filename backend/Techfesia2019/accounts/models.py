from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from django.db.models import signals
from django.dispatch import receiver

from events.models import Event, SoloEvent
from registration.models import User

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    profile_pic = models.URLField()
    phone_number = models.CharField(max_length=13, validators=[MinLengthValidator(13)], null=True, blank=True)
    college_name = models.CharField(max_length=150, null=True, blank=True)


class ProfileParticipant(models.Model):
    profile = models.OneToOneField(to=Profile, on_delete=models.CASCADE)


class ProfileOrganizer(models.Model):
    profile = models.OneToOneField(to=Profile, on_delete=models.CASCADE)
    events = models.ManyToManyField(to=Event, related_name="organizers")


class ProfileVolunteer(models.Model):
    profile = models.OneToOneField(to=Profile, on_delete=models.CASCADE)
    events = models.ManyToManyField(to=Event, related_name="volunteers")



@receiver(signals.post_save, sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
    """
        If user is superuser, then set email confirmed to true
    """

    if created:
        profile =Profile(user=instance)
        profile.save()
