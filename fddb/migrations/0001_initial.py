# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 16:37
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
            name='Fddb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organismo', models.CharField(choices=[('BR1', 'BR174'), ('COA', 'Coari'), ('MAN', 'Manicoré')], default='BR1', max_length=64)),
                ('folha', models.CharField(max_length=4)),
                ('complemento', models.CharField(blank=True, max_length=16, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'fddbs',
                'ordering': ['organismo'],
                'verbose_name': 'fddb',
            },
            bases=(models.Model, projeto.models.template.TemplateModelMixin),
        ),
    ]
