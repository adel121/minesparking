# Generated by Django 4.0.1 on 2022-01-26 14:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0009_remove_occupies_entry_time_drives_car_pub_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drives_car',
            name='Pub_Time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 14, 21, 52, 826264, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pending_request',
            name='Last_Captured',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 14, 21, 52, 826640, tzinfo=utc)),
        ),
    ]
