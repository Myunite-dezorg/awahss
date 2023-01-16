# Generated by Django 4.1.4 on 2023-01-16 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.CharField(blank=True, max_length=15, null=True)),
                ('barcode', models.ImageField(blank=True, upload_to='agents/barcodes/')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile', verbose_name='profile_agent')),
            ],
        ),
    ]
