# Generated by Django 4.0.4 on 2022-04-27 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_location_participant_meetup_participant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='Participant',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
    ]
