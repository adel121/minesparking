# Generated by Django 4.0.1 on 2022-01-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0002_pending_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='pending_request',
            name='Status',
            field=models.CharField(choices=[('pending', 'pending'), ('in progress', 'in progress'), ('verified', 'verified')], default='pending', max_length=100),
        ),
    ]
