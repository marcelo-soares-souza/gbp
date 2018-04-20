from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from projeto.models.objetivo import Objetivo
from projeto.models.projeto import Projeto
from projeto.models.template import TemplateModelMixin

from smart_selects.db_fields import ChainedManyToManyField


#
# Objetivo de Projetos
#

class MetaProjeto(models.Model, TemplateModelMixin):

    numero = models.IntegerField(default=1)
    nome = models.CharField(max_length=256, validators=[
                            MinLengthValidator(5)])
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
        ordering = ['nome']
        verbose_name = 'meta'
        verbose_name_plural = 'metas'

    def __str__(self):
        return 'MT%d: %s' % (self.numero, self.nome)
