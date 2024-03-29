# Generated by Django 2.0.4 on 2021-10-20 16:38

from django.db import migrations, models
import django.db.models.deletion
import projeto.models.template


class Migration(migrations.Migration):

    dependencies = [
        ('ssrnai', '0026_auto_20211016_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Percevejo_Asiatico_Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('halys_whole1', models.FloatField(blank=True, null=True, verbose_name='halys_whole1')),
                ('halys_whole2', models.FloatField(blank=True, null=True, verbose_name='halys_whole2')),
                ('halys_antennae1', models.FloatField(blank=True, null=True, verbose_name='halys_antennae1')),
                ('halys_gut', models.FloatField(blank=True, null=True, verbose_name='halys_gut')),
                ('halys_antennae2', models.FloatField(blank=True, null=True, verbose_name='halys_antennae2')),
                ('halys_antennae3', models.FloatField(blank=True, null=True, verbose_name='halys_antennae3')),
                ('halys_salivary1', models.FloatField(blank=True, null=True, verbose_name='halys_salivary1')),
                ('halys_salivary2', models.FloatField(blank=True, null=True, verbose_name='halys_salivary2')),
                ('halys_salivary3', models.FloatField(blank=True, null=True, verbose_name='halys_salivary3')),
                ('halys_salivary4', models.FloatField(blank=True, null=True, verbose_name='halys_salivary4')),
                ('gene', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ssrnai.Percevejo_Gene_Information')),
                ('organism', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ssrnai.Organisms')),
            ],
            options={
                'verbose_name': 'halys_expression',
                'verbose_name_plural': 'halys_expressions',
                'ordering': ['id'],
            },
            bases=(models.Model, projeto.models.template.TemplateModelMixin),
        ),
        migrations.AddField(
            model_name='conyza_gene_information',
            name='dataset',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='dataset'),
        ),
    ]
