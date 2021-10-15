# Generated by Django 2.0.4 on 2021-10-15 13:58

from django.db import migrations, models
import django.db.models.deletion
import projeto.models.template


class Migration(migrations.Migration):

    dependencies = [
        ('ssrnai', '0017_auto_20211015_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conyza_Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q17_R1_POST', models.FloatField(blank=True, null=True, verbose_name='Q17_R1_POST')),
                ('Q17_R1_PRE', models.FloatField(blank=True, null=True, verbose_name='Q17_R1_PRE')),
                ('Q17_R5_POST', models.FloatField(blank=True, null=True, verbose_name='Q17_R5_POST')),
                ('Q17_R5_PRE', models.FloatField(blank=True, null=True, verbose_name='Q17_R5_PRE')),
                ('Q21_S4_POST', models.FloatField(blank=True, null=True, verbose_name='Q21_S4_POST')),
                ('Q21_S4_PRE', models.FloatField(blank=True, null=True, verbose_name='Q21_S4_PRE')),
                ('Q21_S5_POST', models.FloatField(blank=True, null=True, verbose_name='Q21_S5_POST')),
                ('Q21_S5_PRE', models.FloatField(blank=True, null=True, verbose_name='Q21_S5_PRE')),
                ('Q21_S7_POST', models.FloatField(blank=True, null=True, verbose_name='Q21_S7_POST')),
                ('Q21_S7_PRE', models.FloatField(blank=True, null=True, verbose_name='Q21_S7_PRE')),
                ('Q34_S1_POST', models.FloatField(blank=True, null=True, verbose_name='Q34_S1_POST')),
                ('Q34_S1_PRE', models.FloatField(blank=True, null=True, verbose_name='Q34_S1_PRE')),
                ('Q34_S2_POST', models.FloatField(blank=True, null=True, verbose_name='Q34_S2_POST')),
                ('Q34_S2_PRE', models.FloatField(blank=True, null=True, verbose_name='Q34_S2_PRE')),
                ('Q34_S5_POST', models.FloatField(blank=True, null=True, verbose_name='Q34_S5_POST')),
                ('Q34_S5_PRE', models.FloatField(blank=True, null=True, verbose_name='Q34_S5_PRE')),
                ('Q42_R4_POST', models.FloatField(blank=True, null=True, verbose_name='Q42_R4_POST')),
                ('Q42_R4_PRE', models.FloatField(blank=True, null=True, verbose_name='Q42_R4_PRE')),
                ('Q42_R5_POST', models.FloatField(blank=True, null=True, verbose_name='Q42_R5_POST')),
                ('Q42_R5_PRE', models.FloatField(blank=True, null=True, verbose_name='Q42_R5_PRE')),
                ('Q42_R6_POST', models.FloatField(blank=True, null=True, verbose_name='Q42_R6_POST')),
                ('Q42_R6_PRE', models.FloatField(blank=True, null=True, verbose_name='Q42_R6_PRE')),
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
        migrations.CreateModel(
            name='Nematoide_Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MI_egg_2', models.FloatField(blank=True, null=True, verbose_name='MI_egg_2')),
                ('MI_J3_3', models.FloatField(blank=True, null=True, verbose_name='MI_J3_3')),
                ('MI_J4_3', models.FloatField(blank=True, null=True, verbose_name='MI_J4_3')),
                ('MI_J4_2', models.FloatField(blank=True, null=True, verbose_name='MI_J4_2')),
                ('MI_egg_1', models.FloatField(blank=True, null=True, verbose_name='MI_egg_1')),
                ('MI_J4_1', models.FloatField(blank=True, null=True, verbose_name='MI_J4_1')),
                ('MI_female_2', models.FloatField(blank=True, null=True, verbose_name='MI_female_2')),
                ('MI_female_1', models.FloatField(blank=True, null=True, verbose_name='MI_female_1')),
                ('MI_female_3', models.FloatField(blank=True, null=True, verbose_name='MI_female_3')),
                ('MI_J2_2', models.FloatField(blank=True, null=True, verbose_name='MI_J2_2')),
                ('MI_J3_1', models.FloatField(blank=True, null=True, verbose_name='MI_J2_3')),
                ('MI_J2_3', models.FloatField(blank=True, null=True, verbose_name='MI_J2_3')),
                ('MI_J3_2', models.FloatField(blank=True, null=True, verbose_name='MI_J3_2')),
                ('MI_J2_1', models.FloatField(blank=True, null=True, verbose_name='MI_J2_1')),
                ('MI_egg_3', models.FloatField(blank=True, null=True, verbose_name='MI_egg_3')),
                ('Nig_2_Rep3', models.FloatField(blank=True, null=True, verbose_name='Nig_2_Rep3')),
                ('Nig_2_Rep2', models.FloatField(blank=True, null=True, verbose_name='Nig_2_Rep2')),
                ('Ken_1_Rep2', models.FloatField(blank=True, null=True, verbose_name='Ken_1_Rep2')),
                ('Nig_3_Rep1', models.FloatField(blank=True, null=True, verbose_name='Nig_3_Rep1')),
                ('Nig_2_Rep1', models.FloatField(blank=True, null=True, verbose_name='Nig_2_Rep1')),
                ('Nig_1_Rep3', models.FloatField(blank=True, null=True, verbose_name='Nig_1_Rep3')),
                ('Nig_1_Rep2', models.FloatField(blank=True, null=True, verbose_name='Nig_1_Rep2')),
                ('Nig_1_Rep1', models.FloatField(blank=True, null=True, verbose_name='Nig_1_Rep1')),
                ('Ken_1_Rep3', models.FloatField(blank=True, null=True, verbose_name='Ken_1_Rep3')),
                ('Nig_3_Rep2', models.FloatField(blank=True, null=True, verbose_name='Nig_3_Rep2')),
                ('Nig_3_Rep3', models.FloatField(blank=True, null=True, verbose_name='Nig_3_Rep3')),
                ('Ken_1_Rep1', models.FloatField(blank=True, null=True, verbose_name='Ken_1_Rep1')),
                ('gene', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ssrnai.Nematoide_Gene_Information')),
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