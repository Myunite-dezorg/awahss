# Generated by Django 4.1.4 on 2023-01-17 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Payload title')),
                ('type', models.CharField(choices=[('cargo', 'cargo'), ('mail', 'mail'), ('equipments', 'equipments')], default='cargo', max_length=50)),
                ('messages', models.TextField()),
                ('createAt', models.DateTimeField(auto_now=True)),
                ('updateAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
