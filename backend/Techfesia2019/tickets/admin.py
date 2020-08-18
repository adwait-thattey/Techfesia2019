from django.contrib import admin
from .models import Ticket, TicketComment


admin.site.register(Ticket);
admin.site.register(TicketComment);
# Register your models here.
