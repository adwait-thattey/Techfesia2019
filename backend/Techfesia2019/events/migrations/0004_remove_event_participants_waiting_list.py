# Generated by Django 2.2.2 on 2019-07-01 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_participants_waiting_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='participants_waiting_list',
        ),
    ]