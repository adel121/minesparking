# Generated by Django 4.0.1 on 2022-01-17 22:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0007_alter_pending_request_last_captured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_request',
            name='Last_Captured',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 17, 22, 21, 17, 674122, tzinfo=utc)),
        ),
    ]
