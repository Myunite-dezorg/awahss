# Generated by Django 4.0.10 on 2023-03-05 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aogorder',
            name='service_request',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='services.aogservice'),
        ),
    ]
