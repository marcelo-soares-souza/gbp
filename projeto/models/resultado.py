from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedManyToManyField

from projeto.models.objetivo import Objetivo
from projeto.models.projeto import Projeto


#
# Resultado de Objetivos
#

class Resultado(models.Model):

    numero = models.PositiveIntegerField(blank=True)
    descricao = models.TextField(null=True, blank=True)
    projeto = models.ForeignKey(Projeto, null=True, blank=True)

    objetivo = ChainedManyToManyField(
        Objetivo,
        chained_field="projeto",
        chained_model_field="projeto",
    )

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['numero']
        verbose_name = 'resultado'
        verbose_name_plural = 'resultados'

    def get_resultado_detail_url(self):
        return u"/resultado/detail/%i" % self.id

    def get_resultado_update_url(self):
        return u"/resultado/update/%i" % self.id

    def get_resultado_delete_url(self):
        return u"/resultado/delete/%i" % self.id

    def __str__(self):
        return 'RE%d: %s' % (self.numero, self.descricao)
