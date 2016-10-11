# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 12:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import projeto.models.template


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('metabolomica', '0002_experiment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'equipment',
                'verbose_name_plural': 'equipments',
                'ordering': ['name'],
            },
            bases=(models.Model, projeto.models.template.TemplateModelMixin),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_code', models.CharField(max_length=120)),
                ('experimental_condition', models.TextField(blank=True, null=True)),
                ('equip_mode', models.CharField(max_length=40)),
                ('data_criado', models.DateTimeField(auto_now_add=True)),
                ('data_modificado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='metabolomica.Equipment')),
            ],
            options={
                'verbose_name': 'result',
                'verbose_name_plural': 'results',
                'ordering': ['sample_code'],
            },
            bases=(models.Model, projeto.models.template.TemplateModelMixin),
        ),
    ]
