from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.utils import timezone

from projeto.models.template import TemplateModelMixin
from projeto.models.instituicao import Instituicao

'''
Classe Modelo de Projeto. Principal classe do sistema, que possui
todas as informações de um projeto {seja em atributos e/ou
elacionamentos com as outras classes}
'''


class Projeto(models.Model, TemplateModelMixin):
    STATUS = (
        ('PLAN', 'Planejamento'),
        ('AVAL', 'Em Avaliação'),
        ('EXEC', 'Em Execução'),
        ('FINA', 'Finalizado'),
    )

    seg = models.CharField(max_length=32, validators=[
                           MinLengthValidator(2)], blank=True)

    titulo_portugues = models.CharField(
        max_length=256, validators=[MinLengthValidator(5)])

    titulo_ingles = models.CharField(max_length=256, validators=[
                                     MinLengthValidator(5)], blank=True)

    sigla = models.CharField(max_length=64, validators=[MinLengthValidator(2)])

    data_inicio = models.DateField(blank=True, null=True, default=timezone.now)

    duracao = models.IntegerField(blank=True, default=1)
    hipotese = models.TextField(blank=True)
    objetivo_geral = models.TextField(blank=True)
    resumo = models.TextField(blank=True)
    status = models.CharField(max_length=64, choices=STATUS, default='PLAN')
    lider = models.ForeignKey(
        User, null=True, blank=True, related_name='lider')

    instituicao_proponente = models.ForeignKey(
        Instituicao, related_name='proponente', null=True, blank=True)
    instituicao_executora = models.ForeignKey(
        Instituicao, related_name='executora', null=True, blank=True)
    projeto_relacionado = models.ForeignKey(
        'self', related_name='relacionado', null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(
        User, null=True, blank=True, related_name='criado')

    class Meta:
        ordering = ['sigla']
        verbose_name = 'projeto'
        verbose_name_plural = 'projetos'

    def __str__(self):
        return self.sigla

    def status_verbose(self):
        return dict(Projeto.STATUS)[self.status]
