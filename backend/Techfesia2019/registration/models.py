from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    """
    Extended from Abstract User
    List of inherited fields: first_name, last_name, email, username, password
    """