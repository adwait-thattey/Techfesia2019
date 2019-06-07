from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    dob = models.DateField(default=now().date().today())
    phone_number = models.CharField(max_length=13, unique=True)
    college_name = models.CharField(max_length=50)
    profile_picture = models.CharField(max_length=200, default='profiles_pictures/abstract_user.jpg')
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
