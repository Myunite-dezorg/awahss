# Generated by Django 4.1.4 on 2023-01-17 22:16

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Category name')),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='wrhs.dcategory', verbose_name='Subdivision')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'unique_together': {('parent', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='DGRClass',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('dgr_class', models.IntegerField(verbose_name='Class')),
                ('description', models.TextField(verbose_name='Description')),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('imp_code', models.CharField(default='...', max_length=3, verbose_name='Imp code1')),
                ('imp_code2', models.CharField(default='', max_length=3, verbose_name='Imp code2')),
                ('imp_code3', models.CharField(default='', max_length=3, verbose_name='Imp code3')),
                ('cao', models.BooleanField(default=False, verbose_name='CAO')),
                ('dgr_label', models.ImageField(null=True, upload_to='wrh/dgr/labels/', verbose_name='Label')),
                ('remarks', models.TextField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dgr_category', to='wrhs.dcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
