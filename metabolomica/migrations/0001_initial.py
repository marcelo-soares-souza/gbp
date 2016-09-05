# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-05 13:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import projeto.models.template


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'sample',
                'verbose_name_plural': 'samples',
                'ordering': ['name'],
            },
            bases=(models.Model, projeto.models.template.TemplateModelMixin),
        ),
    ]
