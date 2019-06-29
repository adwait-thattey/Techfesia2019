# Generated by Django 2.2.2 on 2019-06-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20190628_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Opened', 'Opened'), ('In Progress', 'In Progress'), ('Solved', 'Solved')], default='Opened', max_length=20),
        ),
    ]