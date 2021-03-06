# Generated by Django 3.2.3 on 2022-01-28 12:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0012_alter_drives_car_pub_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(choices=[('allowed', 'allowed'), ('not allowed', 'not allowed')], default='not allowed', max_length=100)),
                ('LastAllowed', models.DateTimeField(default=datetime.datetime(2022, 1, 28, 12, 47, 52, 529706, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='drives_car',
            name='Pub_Time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 12, 47, 52, 528873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pending_request',
            name='Last_Captured',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 12, 47, 52, 529328, tzinfo=utc)),
        ),
    ]
