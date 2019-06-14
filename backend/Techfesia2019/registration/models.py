from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    """
    Extended from Abstract User
    List of inherited fields: first_name, last_name, email, username, password
    """


class FirebaseUser(models.Model):
    """
    Stores all the details that come from the users firebase account using O-Auth
    """
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    uid = models.CharField(max_length=150)
    profile_pic_url = models.URLField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)