# Generated by Django 2.0.4 on 2021-09-23 19:39

from django.db import migrations, models
import projeto.models.template


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'database',
                'verbose_name_plural': 'databases',
                'ordering': ['name'],
            },
            bases=(models.Model, projeto.models.template.TemplateModelMixin),
        ),
    ]
