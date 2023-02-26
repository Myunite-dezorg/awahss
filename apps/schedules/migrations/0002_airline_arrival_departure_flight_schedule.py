# Generated by Django 4.1.7 on 2023-02-26 21:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iataCode', models.CharField(blank=True, max_length=3, null=True, verbose_name='Iata code')),
                ('icaoCode', models.CharField(blank=True, max_length=4, null=True, verbose_name='Icao code')),
                ('name', models.CharField(blank=True, max_length=4, null=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actualTime', models.DateTimeField()),
                ('baggage', models.IntegerField()),
                ('delay', models.IntegerField()),
                ('estimatedRunway', models.DateTimeField()),
                ('estimatedTime', models.DateTimeField()),
                ('gate', models.IntegerField()),
                ('iataCode', models.CharField(blank=True, max_length=4, null=True, verbose_name='Iata code')),
                ('icaoCode', models.CharField(blank=True, max_length=4, null=True, verbose_name='Icao code')),
                ('scheduledTime', models.DateTimeField()),
                ('terminal', models.CharField(blank=True, max_length=3, null=True, verbose_name='Terminal')),
            ],
        ),
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actualTime', models.DateTimeField()),
                ('baggage', models.IntegerField()),
                ('delay', models.IntegerField()),
                ('estimatedRunway', models.DateTimeField()),
                ('estimatedTime', models.DateTimeField()),
                ('gate', models.IntegerField()),
                ('iataCode', models.CharField(blank=True, max_length=4, null=True, verbose_name='Iata code')),
                ('icaoCode', models.CharField(blank=True, max_length=4, null=True, verbose_name='Icao code')),
                ('scheduledTime', models.DateTimeField()),
                ('terminal', models.CharField(blank=True, max_length=3, null=True, verbose_name='Terminal')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iataNumber', models.CharField(blank=True, max_length=5, null=True, verbose_name='Iata number')),
                ('icaoNumber', models.CharField(blank=True, max_length=10, null=True, verbose_name='Icao number')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('createAt', models.DateTimeField(auto_now=True)),
                ('updateAt', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True, verbose_name='Status')),
                ('type', models.CharField(blank=True, max_length=20, null=True, verbose_name='Type')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
