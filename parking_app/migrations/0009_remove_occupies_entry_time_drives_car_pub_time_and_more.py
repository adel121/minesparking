# Generated by Django 4.0.1 on 2022-01-24 17:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0008_alter_pending_request_last_captured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occupies',
            name='Entry_Time',
        ),
        migrations.AddField(
            model_name='drives_car',
            name='Pub_Time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 17, 23, 37, 217443, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pending_request',
            name='Last_Captured',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 17, 23, 37, 217759, tzinfo=utc)),
        ),
    ]
