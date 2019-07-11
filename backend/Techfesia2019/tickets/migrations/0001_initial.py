# Generated by Django 2.2.2 on 2019-06-28 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_profile_user'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(blank=True, db_index=True, max_length=100, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('opening_date', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('O', 'Opened'), ('P', 'In Progress'), ('S', 'Solved')], default='O', max_length=1)),
                ('solving_date', models.DateField(blank=True, null=True)),
                ('content', models.CharField(max_length=2000)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('opened_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
                ('solved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solved_tickets', to='accounts.Profile')),
                ('subscribers', models.ManyToManyField(related_name='subscribed_tickets', to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(blank=True, db_index=True, max_length=100, unique=True)),
                ('text', models.CharField(max_length=1000)),
                ('posting_date', models.DateTimeField()),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opened_tickets', to='accounts.Profile')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket')),
            ],
        ),
    ]
