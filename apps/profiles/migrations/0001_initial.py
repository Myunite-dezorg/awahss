# Generated by Django 4.1.7 on 2023-02-26 20:17

import birthday.fields
from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='First Name')),
                ('second_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Second Name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Last Name')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='Position')),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('shift_work', models.BooleanField(default=0, verbose_name='Shift sched?')),
                ('birthday_dayofyear_internal', models.PositiveSmallIntegerField(default=None, editable=False, null=True)),
                ('birthday', birthday.fields.BirthdayField(null=True)),
                ('avatar', models.ImageField(upload_to='images/users/')),
            ],
        ),
    ]
