# Generated by Django 2.0.4 on 2021-10-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssrnai', '0009_percevejo_expression'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='percevejo_structure',
            options={'ordering': ['id'], 'verbose_name': 'structure', 'verbose_name_plural': 'structures'},
        ),
        migrations.AlterField(
            model_name='percevejo_structure',
            name='classification',
            field=models.CharField(max_length=50, null=True, verbose_name='classification'),
        ),
        migrations.AlterField(
            model_name='percevejo_structure',
            name='composition',
            field=models.TextField(blank=True, null=True, verbose_name='composition'),
        ),
        migrations.AlterField(
            model_name='percevejo_structure',
            name='figure',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='figure'),
        ),
        migrations.AlterField(
            model_name='percevejo_structure',
            name='interaction_energy',
            field=models.FloatField(blank=True, max_length=50, null=True, verbose_name='interaction_energy'),
        ),
        migrations.AlterField(
            model_name='percevejo_structure',
            name='match',
            field=models.IntegerField(blank=True, null=True, verbose_name='match'),
        ),
        migrations.AlterField(
            model_name='percevejo_structure',
            name='mismatch',
            field=models.IntegerField(blank=True, null=True, verbose_name='mismatch'),
        ),
    ]
