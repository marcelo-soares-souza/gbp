from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from datetime import datetime

from projeto.models.tipo import Tipo
from projeto.models.status import Status
from projeto.models.instituicao import Instituicao

'''
Classe Modelo de Projeto. Principal classe do sistema, que possui
todas as informações de um projeto {seja em atributos e/ou
elacionamentos com as outras classes}
'''


class Projeto(models.Model):

    seg = models.CharField(max_length=32, validators=[
                           MinLengthValidator(2)], blank=True)

    titulo_portugues = models.CharField(max_length=256, validators=[MinLengthValidator(5)])

    titulo_ingles = models.CharField(max_length=256, validators=[MinLengthValidator(5)], blank=True)

    sigla = models.CharField(max_length=64, validators=[MinLengthValidator(2)])

    data_inicio = models.DateField(blank=True, null=True, default=datetime.now)

    duracao = models.IntegerField(blank=True, default=1)
    hipotese = models.TextField(blank=True)
    objetivo_geral = models.TextField(blank=True)
    resumo = models.TextField(blank=True)
    tipo = models.ForeignKey(Tipo, null=True, blank=True, related_name='tipo')
    status = models.ForeignKey(
        Status, null=True, blank=True, related_name='status')
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

    def get_projeto_detail_url(self):
        return u"/detail/%i" % self.id

    def get_projeto_update_url(self):
        return u"/update/%i" % self.id

    def get_projeto_delete_url(self):
        return u"/delete/%i" % self.id

    def __str__(self):
        return self.sigla
