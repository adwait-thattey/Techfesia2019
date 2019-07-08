import os

from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from registration.models import User

def set_file_upload_path(instance, filename):
    if instance.forced_filename:
        return os.path.join(instance.upload_path, instance.forced_filename)
    else:
        return os.path.join(instance.upload_path, filename)

class FileUploadModel(models.Model):
    """
    A common model to keep track of all uploads
    """
    purpose = models.CharField(max_length=100)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    upload_path = models.CharField(max_length=250)
    forced_filename = models.CharField(max_length=80, null=True, blank=True)
    uploaded_file = models.FileField(upload_to=set_file_upload_path)
    additional_info = models.TextField(null=True, blank=True)

    def clean(self):
        if self.upload_path[0] == '/':
            raise ValidationError({
                'upload_path':"Absolute paths are not allowed. If you are passing relative paths, remove the preceding '/'"
            })