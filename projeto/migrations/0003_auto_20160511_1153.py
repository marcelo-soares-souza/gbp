# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0002_auto_20160511_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projeto.Projeto'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projeto.Projeto'),
        ),
    ]
