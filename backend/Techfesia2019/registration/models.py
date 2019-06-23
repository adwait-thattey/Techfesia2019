from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import signals
from django.dispatch import receiver


class User(AbstractUser):
    """
    Extended from Abstract User
    List of inherited fields: first_name, last_name, email, username, password
    """

    email_confirmed = models.BooleanField(default=False)


class FirebaseUser(models.Model):
    """
    Stores all the details that come from the users firebase account using O-Auth
    """
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=150, unique=True)
    profile_pic_url = models.URLField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

@receiver(signals.post_save, sender=User)
def set_email_confirmed_true_for_superuser(sender, instance, created, **kwargs):
    """
        If user is superuser, then set email confirmed to true
    """

    if created and instance.is_superuser:
        instance.email_confirmed = True
        instance.save()


@receiver(signals.post_save, sender=FirebaseUser)
def set_email_confirmed_true_for_oauth(sender, instance, created, **kwargs):
    """
        If user is coming from o-auth, then set email confirmed to true
    """

    if created:
        instance.user.email_confirmed = True
        instance.user.save()