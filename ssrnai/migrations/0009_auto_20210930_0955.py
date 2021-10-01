# Generated by Django 2.0.4 on 2021-09-30 12:55

from django.db import migrations, models
import django.db.models.deletion
import projeto.models.template


class Migration(migrations.Migration):

    dependencies = [
        ('ssrnai', '0008_auto_20210930_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organism_name', models.CharField(max_length=150, unique=True, verbose_name='organism_name')),
                ('common_name', models.CharField(max_length=150, verbose_name='common_name')),
                ('taxonomy', models.CharField(blank=True, max_length=1000, null=True, verbose_name='taxonomy')),
                ('database', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ssrnai.Database')),
            ],
            options={
                'verbose_name': 'organism',
                'verbose_name_plural': 'organisms',
                'ordering': ['organism_name'],
            },
            bases=(models.Model, projeto.models.template.TemplateModelMixin),
        ),
        migrations.RemoveField(
            model_name='organism',
            name='database',
        ),
        migrations.DeleteModel(
            name='Organism',
        ),
    ]
