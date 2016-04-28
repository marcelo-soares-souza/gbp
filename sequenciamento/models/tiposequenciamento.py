from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

from projeto.models.projeto import Projeto


class TipoSequenciamento(models.Model):
    nome = models.CharField(max_length=256, blank=True)
    descricao = models.TextField(null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'tiposequenciamento'
        verbose_name_plural = 'tiposequenciamentos'

    def get_tiposequenciamento_detail_url(self):
        return u"/tiposequenciamento/detail/%i" % self.id

    def get_tiposequenciamento_update_url(self):
        return u"/tiposequenciamento/update/%i" % self.id

    def get_tiposequenciamento_delete_url(self):
        return u"/tiposequenciamento/delete/%i" % self.id

    def __str__(self):
        return '%s %s' % (self.nome, self.descricao)

'''
class Sequenciamento(models.Model):
    projeto = models.ForeignKey(Projeto)
    tipo_sequenciamento = models.ForeignKey(TipoSequenciamento)
    responsavel = models.ForeignKey(
        User, null=True, blank=True, related_name='responsavel')
    objetivo = models.TextField(null=True, blank=True)
    material_biologico = models.CharField(max_length=256, blank=True)
    descricao_material_biologico = models.TextField(null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)
'''
