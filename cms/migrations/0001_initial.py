# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 13:31
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
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
            name='Pagina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256, validators=[django.core.validators.MinLengthValidator(5)])),
                ('texto', models.TextField(blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['titulo'],
                'verbose_name_plural': 'paginas',
                'verbose_name': 'pagina',
            },
            bases=(models.Model, projeto.models.template.TemplateModelMixin),
        ),
    ]
