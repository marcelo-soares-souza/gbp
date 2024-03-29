# Generated by Django 2.0.4 on 2021-10-27 14:24

from django.db import migrations, models
import django.db.models.deletion
import projeto.models.template


class Migration(migrations.Migration):

    dependencies = [
        ('ssrnai', '0027_auto_20211020_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conyza_Canadensis_Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Water_1T_r1', models.FloatField(blank=True, null=True, verbose_name='Water_1T_r1')),
                ('Water_1T_r2', models.FloatField(blank=True, null=True, verbose_name='Water_1T_r2')),
                ('Water_1T_r3', models.FloatField(blank=True, null=True, verbose_name='Water_1T_r3')),
                ('Water_1T_r4', models.FloatField(blank=True, null=True, verbose_name='Water_1T_r4')),
                ('Water_6T_r1', models.FloatField(blank=True, null=True, verbose_name='Water_6T_r1')),
                ('Water_6T_r2', models.FloatField(blank=True, null=True, verbose_name='Water_6T_r2')),
                ('Water_6T_r3', models.FloatField(blank=True, null=True, verbose_name='Water_6T_r3')),
                ('Water_6T_r4', models.FloatField(blank=True, null=True, verbose_name='Water_6T_r4')),
                ('D_2_4_1T_r1', models.FloatField(blank=True, null=True, verbose_name='D_2_4_1T_r1')),
                ('D_2_4_1T_r2', models.FloatField(blank=True, null=True, verbose_name='D_2_4_1T_r2')),
                ('D_2_4_1T_r3', models.FloatField(blank=True, null=True, verbose_name='D_2_4_1T_r3')),
                ('D_2_4_1T_r4', models.FloatField(blank=True, null=True, verbose_name='D_2_4_1T_r4')),
                ('D_2_4_6T_r1', models.FloatField(blank=True, null=True, verbose_name='D_2_4_6T_r1')),
                ('D_2_4_6T_r2', models.FloatField(blank=True, null=True, verbose_name='D_2_4_6T_r2')),
                ('D_2_4_6T_r3', models.FloatField(blank=True, null=True, verbose_name='D_2_4_6T_r3')),
                ('D_2_4_6T_r4', models.FloatField(blank=True, null=True, verbose_name='D_2_4_6T_r4')),
                ('Dicamba_1T_r1', models.FloatField(blank=True, null=True, verbose_name='Dicamba_1T_r1')),
                ('Dicamba_1T_r2', models.FloatField(blank=True, null=True, verbose_name='Dicamba_1T_r2')),
                ('Dicamba_1T_r3', models.FloatField(blank=True, null=True, verbose_name='Dicamba_1T_r3')),
                ('Dicamba_1T_r4', models.FloatField(blank=True, null=True, verbose_name='Dicamba_1T_r4')),
                ('Dicamba_6T_r1', models.FloatField(blank=True, null=True, verbose_name='Dicamba_6T_r1')),
                ('Dicamba_6T_r2', models.FloatField(blank=True, null=True, verbose_name='Dicamba_6T_r2')),
                ('Dicamba_6T_r3', models.FloatField(blank=True, null=True, verbose_name='Dicamba_6T_r3')),
                ('Dicamba_6T_r4', models.FloatField(blank=True, null=True, verbose_name='Dicamba_6T_r4')),
                ('HM_1T_r1', models.FloatField(blank=True, null=True, verbose_name='HM_1T_r1')),
                ('HM_1T_r2', models.FloatField(blank=True, null=True, verbose_name='HM_1T_r2')),
                ('HM_1T_r3', models.FloatField(blank=True, null=True, verbose_name='HM_1T_r3')),
                ('HM_1T_r4', models.FloatField(blank=True, null=True, verbose_name='HM_1T_r4')),
                ('HM_6T_r1', models.FloatField(blank=True, null=True, verbose_name='HM_6T_r1')),
                ('HM_6T_r2', models.FloatField(blank=True, null=True, verbose_name='HM_6T_r2')),
                ('HM_6T_r3', models.FloatField(blank=True, null=True, verbose_name='HM_6T_r3')),
                ('HM_6T_r4', models.FloatField(blank=True, null=True, verbose_name='HM_6T_r4')),
                ('gene', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ssrnai.Conyza_Gene_Information')),
                ('organism', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ssrnai.Organisms')),
            ],
            options={
                'verbose_name': 'expression',
                'verbose_name_plural': 'expressions',
                'ordering': ['id'],
            },
            bases=(models.Model, projeto.models.template.TemplateModelMixin),
        ),
    ]
