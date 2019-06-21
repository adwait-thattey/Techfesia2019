# Generated by Django 2.2.2 on 2019-06-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='public_id',
            field=models.CharField(default='123', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='Hello', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]