# Generated by Django 4.1.7 on 2023-02-26 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile', verbose_name='profile_company'),
        ),
        migrations.AddField(
            model_name='agent',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile', verbose_name='profile_agent'),
        ),
    ]
