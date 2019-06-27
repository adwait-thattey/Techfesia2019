from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from accounts.models import Profile
from base.utils import generate_public_id
from django.utils.translation import gettext_lazy as _

from events.models import SoloEvent, TeamEvent


class Team(models.Model):
    public_id = models.CharField(max_length=100,
                                 unique=True,
                                 blank=True,
                                 db_index=True)

    name = models.CharField(max_length=20,
                            unique=True,
                            db_index=True
                            )

    team_leader = models.ForeignKey(to=Profile,
                                    on_delete=models.PROTECT
                                    )

    create_date = models.DateTimeField(auto_now_add=True)

    @property
    def invitees(self):
        return self.teammember_set.filter(invitation_accepted=False)

    @property
    def member_count(self):
        return self.teammember_set.filter(invitation_accepted=True).count()

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = generate_public_id(self)

        super().save(*args, **kwargs)


class TeamMember(models.Model):
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE, related_name='teammember_set')

    profile = models.ForeignKey(to=Profile, on_delete=models.PROTECT)

    invitation_accepted = models.BooleanField(default=False,
                                              help_text="If true, person has accepted invitation and is part of the team"
                                              )

    joined_on = models.DateTimeField(auto_now=True)

    @property
    def get_user_username(self):
        return self.profile.user.username


class SoloEventRegistration(models.Model):
    public_id = models.CharField(max_length=100,
                                 unique=True,
                                 blank=True,
                                 db_index=True)

    event = models.ForeignKey(to=SoloEvent, on_delete=models.PROTECT)

    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE)

    is_complete = models.BooleanField(default=False,
                                      help_text="Tells whether user has completed all formalities like payments etc."
                                      )

    is_confirmed = models.BooleanField(default=False,
                                       help_text="Tells whether registration is confirmed or is in waiting"
                                       )

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.is_complete is False and self.is_confirmed is True:
            raise ValidationError(_("Registration can not be confirmed until it is complete"))

        if hasattr(self.profile, 'profileorganizer'):

            if self.profile.profileorganizer in self.event.organizers.all():
                raise ValidationError(_("Organizer can not be a participant for the same event"))

        if hasattr(self.profile, 'profilevolunteer'):

            if self.profile.profilevolunteer in self.event.volunteers.all():
                raise ValidationError(_("Volunteer can not be a participant for the same event"))

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = generate_public_id(self)

        super().save(*args, **kwargs)


class TeamEventRegistration(models.Model):
    public_id = models.CharField(max_length=100,
                                 unique=True,
                                 blank=True,
                                 db_index=True)

    event = models.ForeignKey(to=TeamEvent, on_delete=models.PROTECT)

    team = models.ForeignKey(to=Team, on_delete=models.CASCADE, related_name='events')

    is_complete = models.BooleanField(default=False,
                                      help_text="Tells whether the team has completed all formalities like payments etc."
                                      )

    is_confirmed = models.BooleanField(default=False,
                                       help_text="Tells whether registration is confirmed or is in waiting"
                                       )

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

    @property
    def get_event_public_id(self):
        return self.event.public_id

    def clean(self):
        if self.is_complete is False and self.is_confirmed is True:
            raise ValidationError(_("Registration can not be confirmed until it is complete"))

    # TODO: A check required that ensures no team member is an organizer/volunteer for same event
    # Doing it here however might be too expensive

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = generate_public_id(self)

        super().save(*args, **kwargs)
