# Generated by Django 4.1.4 on 2023-01-10 19:51

import apps.directory.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0006_alter_airline_arl_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='arl_logo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.directory.models.airline_logo_directory_path),
        ),
    ]
