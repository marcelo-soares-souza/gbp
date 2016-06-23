from django.contrib.auth.models import User
from django.db import models

from projeto.models.projeto import Projeto
from projeto.models.template import TemplateModelMixin


class Contrato(models.Model, TemplateModelMixin):
    projeto = models.ForeignKey(Projeto)
    empresa_executora = models.CharField(max_length=256, null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['projeto']
        verbose_name = 'contrato'
        verbose_name_plural = 'contratos'

    def __str__(self):
        return '%s - %s' % (self.projeto, self.empresa_executora)
