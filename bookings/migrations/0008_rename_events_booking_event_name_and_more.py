# Generated by Django 5.1.7 on 2025-04-06 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_booking_booking_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='events',
            new_name='event_name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='user',
            new_name='user_name',
        ),
    ]
