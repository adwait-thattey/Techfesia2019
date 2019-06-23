# Generated by Django 2.2.2 on 2019-06-23 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(blank=True, db_index=True, max_length=100, unique=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('event_picture', models.URLField(blank=True, null=True)),
                ('event_logo', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('venue', models.CharField(default='to be determined', max_length=100)),
                ('team_event', models.BooleanField(default=False)),
                ('max_participants', models.IntegerField(default=20)),
                ('reserved_slots', models.IntegerField(default=0, help_text='No of participant slots reserved for external players')),
                ('category', models.ManyToManyField(related_name='events', to='events.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SoloEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
            ],
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='TeamEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
                ('min_team_size', models.IntegerField(default=1)),
                ('max_team_size', models.IntegerField(default=1)),
            ],
            bases=('events.event',),
        ),
        migrations.AddField(
            model_name='event',
            name='participants_waiting_list',
            field=models.ManyToManyField(related_name='waiting_list_events', to='events.Team'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(related_name='events', to='events.Tags'),
        ),
    ]
