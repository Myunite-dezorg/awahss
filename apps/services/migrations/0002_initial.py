# Generated by Django 4.1.4 on 2023-01-17 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
        ('agents', '0002_initial'),
        ('schedules', '0002_alter_regularscheduler_ata_and_more'),
        ('stuffs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dutyperson',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Users persons stuff'),
        ),
        migrations.AddField(
            model_name='aogservice',
            name='aog_item',
            field=models.ManyToManyField(to='stuffs.aog'),
        ),
        migrations.AddField(
            model_name='aogservice',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_created', to='agents.agent', verbose_name='created by'),
        ),
        migrations.AddField(
            model_name='aogservice',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aog_from_flight', to='schedules.regularscheduler'),
        ),
        migrations.AddField(
            model_name='aogservice',
            name='responsibles_persons',
            field=models.ManyToManyField(to='services.dutyperson'),
        ),
        migrations.AddIndex(
            model_name='aogservice',
            index=models.Index(fields=['-type'], name='service_priority_idx'),
        ),
    ]
