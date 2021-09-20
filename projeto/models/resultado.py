from django.contrib.auth.models import User
from django.db import models

from projeto.models.objetivo import Objetivo
from projeto.models.projeto import Projeto
from projeto.models.template import TemplateModelMixin

from smart_selects.db_fields import ChainedManyToManyField


#
# Resultado de Objetivos
#

class Resultado(models.Model, TemplateModelMixin):

    numero = models.PositiveIntegerField(default=1)
    descricao = models.TextField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    objetivo = ChainedManyToManyField(
        Objetivo,
        chained_field="projeto",
        chained_model_field="projeto",
        auto_choose=True,
        blank=True,
    )

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['numero']
        verbose_name = 'resultado'
        verbose_name_plural = 'resultados'

    def __str__(self):
        return 'RE%d: %s' % (self.numero, self.descricao)
