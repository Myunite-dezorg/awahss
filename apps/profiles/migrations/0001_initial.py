# Generated by Django 4.1.4 on 2023-01-08 06:12

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
                ('private_account', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('avatar', models.ImageField(upload_to='images/users/')),
                ('blocked_user', models.ManyToManyField(blank=True, related_name='user_blocked', to='profiles.profile')),
                ('followers', models.ManyToManyField(blank=True, related_name='user_followers', to='profiles.profile')),
                ('following', models.ManyToManyField(blank=True, related_name='user_following', to='profiles.profile')),
                ('panding_request', models.ManyToManyField(blank=True, related_name='pandingRequest', to='profiles.profile')),
            ],
        ),
    ]
