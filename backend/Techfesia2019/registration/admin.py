from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from registration.models import User, FirebaseUser

admin.site.register(User, UserAdmin)

admin.site.register(FirebaseUser)