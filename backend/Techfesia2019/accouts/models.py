from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=12, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=12, null=False, blank=False, unique=True)
    birth_date = models.DateField()
    college_name = models.CharField(null=False,max_length=40)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number', 'birth_date', 'college_name']

    def __str__(self):
        return f'{self.username}'


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='UserProfile')

    def __str__(self):
        return f'{self.user}'
