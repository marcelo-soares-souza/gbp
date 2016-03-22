# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(blank=True)),
                ('nome', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=100, blank=True)),
                ('indicador_fisico', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=32, blank=True)),
                ('peso_planoacao', models.PositiveIntegerField(blank=True)),
                ('data_inicio', models.DateField(blank=True)),
                ('data_fim', models.DateField(blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('colaborador', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='colaborador_atividade', blank=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'atividade',
                'ordering': ['nome'],
                'verbose_name_plural': 'atividades',
            },
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sigla', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=256, blank=True)),
                ('nome', models.CharField(validators=[django.core.validators.MinLengthValidator(5)], max_length=256, blank=True)),
                ('site', models.CharField(validators=[django.core.validators.MinLengthValidator(5)], max_length=128, blank=True)),
                ('email', models.CharField(validators=[django.core.validators.EmailValidator()], max_length=256, blank=True)),
                ('endereco', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=256, blank=True)),
                ('cidade', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=256, blank=True)),
                ('descricao', models.TextField(validators=[django.core.validators.MinLengthValidator(10)], max_length=512, blank=True)),
                ('cnpj', models.CharField(max_length=14, blank=True)),
                ('telefone', models.CharField(max_length=16, blank=True)),
                ('estado', models.CharField(max_length=16, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], blank=True)),
                ('cep', models.CharField(max_length=9, blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'instituição',
                'ordering': ['sigla'],
                'verbose_name_plural': 'instituições',
            },
        ),
        migrations.CreateModel(
            name='MetaProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(blank=True)),
                ('nome', models.CharField(validators=[django.core.validators.MinLengthValidator(5)], max_length=256, blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'meta',
                'ordering': ['nome'],
                'verbose_name_plural': 'metas',
            },
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(blank=True)),
                ('descricao', models.TextField(null=True, blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'objetivo',
                'ordering': ['descricao'],
                'verbose_name_plural': 'objetivos',
            },
        ),
        migrations.CreateModel(
            name='PalavraChave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('palavra', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=32, blank=True)),
                ('descricao', models.CharField(validators=[django.core.validators.MinLengthValidator(3)], null=True, max_length=256, blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'palavra chave',
                'ordering': ['palavra'],
                'verbose_name_plural': 'palavras chaves',
            },
        ),
        migrations.CreateModel(
            name='PlanoAcao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(blank=True)),
                ('nome', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=100)),
                ('codigo_seg', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=32, blank=True)),
                ('data_inicio', models.DateField(blank=True)),
                ('data_fim', models.DateField(blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'plano de ação',
                'ordering': ['nome'],
                'verbose_name_plural': 'planos de ação',
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seg', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=32, blank=True)),
                ('titulo_portugues', models.CharField(validators=[django.core.validators.MinLengthValidator(5)], max_length=256, blank=True)),
                ('titulo_ingles', models.CharField(validators=[django.core.validators.MinLengthValidator(5)], max_length=256, blank=True)),
                ('sigla', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=32, blank=True)),
                ('data_inicio', models.DateField(blank=True)),
                ('duracao', models.IntegerField(blank=True)),
                ('hipotese', models.TextField(blank=True)),
                ('objetivo_geral', models.TextField(blank=True)),
                ('resumo', models.TextField(blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, related_name='criado', to=settings.AUTH_USER_MODEL)),
                ('instituicao_executora', models.ForeignKey(blank=True, null=True, related_name='executora', to='projeto.Instituicao')),
                ('instituicao_proponente', models.ForeignKey(blank=True, null=True, related_name='proponente', to='projeto.Instituicao')),
                ('lider', models.ForeignKey(blank=True, null=True, related_name='lider', to=settings.AUTH_USER_MODEL)),
                ('palavra_chave', models.ManyToManyField(to='projeto.PalavraChave', related_name='palavrachave', blank=True)),
                ('projeto_relacionado', models.ForeignKey(blank=True, null=True, related_name='relacionado', to='projeto.Projeto')),
            ],
            options={
                'verbose_name': 'projeto',
                'ordering': ['sigla'],
                'verbose_name_plural': 'projetos',
            },
        ),
        migrations.CreateModel(
            name='ProjetoComponente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(blank=True)),
                ('nome', models.CharField(validators=[django.core.validators.MinLengthValidator(5)], max_length=256, blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('projeto', models.ForeignKey(to='projeto.Projeto')),
                ('responsavel', models.ForeignKey(blank=True, null=True, related_name='responsavel', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'projeto componente',
                'ordering': ['nome'],
                'verbose_name_plural': 'projetos componentees',
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(blank=True)),
                ('descricao', models.TextField(null=True, blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('objetivo', smart_selects.db_fields.ChainedManyToManyField(to='projeto.Objetivo', chained_model_field='projeto', chained_field='projeto')),
                ('projeto', models.ForeignKey(blank=True, null=True, to='projeto.Projeto')),
            ],
            options={
                'verbose_name': 'resultado',
                'ordering': ['numero'],
                'verbose_name_plural': 'resultados',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=32, blank=True)),
                ('descricao', models.TextField(null=True, blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'status',
                'ordering': ['nome'],
                'verbose_name_plural': 'status',
            },
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(blank=True)),
                ('nome', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=100, blank=True)),
                ('indicador_fisico', models.CharField(validators=[django.core.validators.MinLengthValidator(2)], max_length=32, blank=True)),
                ('peso_atividade', models.PositiveIntegerField(blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('atividade', smart_selects.db_fields.ChainedForeignKey(chained_model_field='planoacao', to='projeto.Atividade', chained_field='planoacao')),
                ('colaborador', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='colaborador_tarefa', blank=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('planoacao', smart_selects.db_fields.ChainedForeignKey(chained_model_field='projeto', to='projeto.PlanoAcao', chained_field='projeto')),
                ('projeto', models.ForeignKey(to='projeto.Projeto', blank=True)),
                ('responsavel', models.ForeignKey(blank=True, null=True, related_name='responsavel_tarefa', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'tarefa',
                'ordering': ['nome'],
                'verbose_name_plural': 'tarefas',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sigla', models.CharField(validators=[django.core.validators.MinLengthValidator(3)], max_length=256, blank=True)),
                ('descricao', models.TextField(null=True, blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizado', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'tipo',
                'ordering': ['sigla'],
                'verbose_name_plural': 'tipos',
            },
        ),
        migrations.AddField(
            model_name='projeto',
            name='status',
            field=models.ForeignKey(blank=True, null=True, related_name='status', to='projeto.Status'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, related_name='tipo', to='projeto.Tipo'),
        ),
        migrations.AddField(
            model_name='planoacao',
            name='projeto',
            field=models.ForeignKey(to='projeto.Projeto', blank=True),
        ),
        migrations.AddField(
            model_name='planoacao',
            name='projeto_componente',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='projeto', to='projeto.ProjetoComponente', chained_field='projeto'),
        ),
        migrations.AddField(
            model_name='planoacao',
            name='responsavel',
            field=models.ForeignKey(blank=True, null=True, related_name='responsavel_plano', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planoacao',
            name='resultado',
            field=smart_selects.db_fields.ChainedManyToManyField(to='projeto.Resultado', chained_model_field='projeto', chained_field='projeto'),
        ),
        migrations.AddField(
            model_name='objetivo',
            name='projeto',
            field=models.ForeignKey(to='projeto.Projeto'),
        ),
        migrations.AddField(
            model_name='metaprojeto',
            name='objetivo',
            field=smart_selects.db_fields.ChainedManyToManyField(to='projeto.Objetivo', chained_model_field='projeto', chained_field='projeto'),
        ),
        migrations.AddField(
            model_name='metaprojeto',
            name='projeto',
            field=models.ForeignKey(blank=True, null=True, to='projeto.Projeto'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='planoacao',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='projeto', to='projeto.PlanoAcao', chained_field='projeto'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='projeto',
            field=models.ForeignKey(to='projeto.Projeto', blank=True),
        ),
        migrations.AddField(
            model_name='atividade',
            name='responsavel',
            field=models.ForeignKey(blank=True, null=True, related_name='responsavel_atividade', to=settings.AUTH_USER_MODEL),
        ),
    ]
