# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0003_auto_20160511_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='Tipo',
        ),
    ]
