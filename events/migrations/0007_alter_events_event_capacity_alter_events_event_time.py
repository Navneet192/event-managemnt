# Generated by Django 5.1.7 on 2025-04-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_events_event_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_capacity',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_time',
            field=models.TimeField(verbose_name=''),
        ),
    ]
