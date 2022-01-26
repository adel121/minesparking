# Generated by Django 4.0.1 on 2022-01-12 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Registry', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Surname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Telephone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('normal', 'normal'), ('anomalous', 'anomalous')], max_length=100)),
                ('Rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Occupies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entry_Time', models.DateTimeField(null=True)),
                ('Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_app.car')),
                ('Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_app.position')),
            ],
        ),
        migrations.CreateModel(
            name='Drives_Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_app.car')),
                ('Driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_app.driver')),
            ],
        ),
    ]
