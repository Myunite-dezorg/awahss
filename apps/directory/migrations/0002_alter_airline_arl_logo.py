# Generated by Django 4.1.4 on 2023-01-08 13:03

import apps.directory.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='arl_logo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.directory.models.airline_logo_directory_path),
        ),
    ]
