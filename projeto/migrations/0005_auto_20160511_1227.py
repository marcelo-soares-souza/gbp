# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0004_auto_20160511_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='criado_por',
        ),
        migrations.AlterField(
            model_name='projeto',
            name='status',
            field=models.CharField(choices=[('PLAN', 'Planejamento'), ('AVAL', 'Em Avaliação'), ('EXEC', 'Em Execução'), ('FINA', 'Finalizado')], default='PLAN', max_length=64),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
