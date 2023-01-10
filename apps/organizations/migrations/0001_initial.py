# Generated by Django 4.1.4 on 2023-01-08 06:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('organization_name', models.CharField(default='Person Company LTD', max_length=50, verbose_name='Company Name')),
                ('address', models.TextField()),
                ('ogrn_number', models.CharField(max_length=13, verbose_name='ОГРН')),
                ('inn_number', models.CharField(max_length=10, verbose_name='ИНН')),
                ('kpp_number', models.CharField(max_length=9, verbose_name='КПП')),
                ('website', models.URLField(verbose_name='Web Site Url')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]