from django.db import models

# Create your models here.
from accounts.models import Profile
from base.utils import generate_public_id


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

    def team_members(self):
        pass

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = generate_public_id(self)

        super().save(*args, **kwargs)


class TeamMember(models.Model):
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE)

    profile = models.ForeignKey(to=Profile, on_delete=models.PROTECT)

    invitation_accepted = models.BooleanField(default=False,
                                              help_text="If true, person has accepted invitation and is part of the team"
                                              )

    joined_on = models.DateTimeField(auto_now=True)
