# Generated by Django 4.1.4 on 2023-01-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrhs', '0007_remove_dgrclass_imp_code1_remove_dgrclass_imp_code2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dgrclass',
            name='imp_code2',
            field=models.CharField(default='', max_length=3, verbose_name='Imp code2'),
        ),
        migrations.AddField(
            model_name='dgrclass',
            name='imp_code3',
            field=models.CharField(default='', max_length=3, verbose_name='Imp code3'),
        ),
        migrations.AlterField(
            model_name='dgrclass',
            name='imp_code',
            field=models.CharField(default='...', max_length=3, verbose_name='Imp code1'),
        ),
    ]
