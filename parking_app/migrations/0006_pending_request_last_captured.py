# Generated by Django 4.0.1 on 2022-01-15 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0005_door'),
    ]

    operations = [
        migrations.AddField(
            model_name='pending_request',
            name='Last_Captured',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 15, 1, 17, 20, 650991)),
        ),
    ]
