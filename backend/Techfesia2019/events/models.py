from django.db import models


# Create your models here.
from base.utils import generate_random_string


class Event(models.Model):
    public_id = models.CharField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = generate_random_string()

        super().save(*args, **kwargs)
