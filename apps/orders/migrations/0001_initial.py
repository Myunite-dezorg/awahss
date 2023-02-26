# Generated by Django 4.1.7 on 2023-02-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AogOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
                ('order_number', models.CharField(editable=False, max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'AOG Order',
                'verbose_name_plural': 'AOG Orders',
            },
        ),
    ]
