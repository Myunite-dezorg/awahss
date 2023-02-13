# Generated by Django 4.1.4 on 2023-02-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_regularscheduler_atd_regularscheduler_ptd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularscheduler',
            name='ata',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='ATA'),
        ),
        migrations.AlterField(
            model_name='regularscheduler',
            name='atd',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='ATA'),
        ),
        migrations.AlterField(
            model_name='regularscheduler',
            name='pta',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='PTA'),
        ),
        migrations.AlterField(
            model_name='regularscheduler',
            name='ptd',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='ATA'),
        ),
        migrations.AlterField(
            model_name='regularscheduler',
            name='sta',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='STA'),
        ),
        migrations.AlterField(
            model_name='regularscheduler',
            name='std',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='ATA'),
        ),
    ]
