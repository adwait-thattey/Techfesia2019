# Generated by Django 2.2.2 on 2019-07-09 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20190630_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcomment',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tickets.Ticket'),
        ),
    ]
