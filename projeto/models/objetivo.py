from django.db import models
from django.contrib.auth.models import User

from projeto.models.template import TemplateModelMixin
from projeto.models.projeto import Projeto

#
# Objetivo Específicos de Projetos
#


class Objetivo(models.Model, TemplateModelMixin):

    # Atributos
    # Número do Objetivo, sequencial e único, mas não é o mesmo número que o id
    numero = models.PositiveIntegerField(default=1)

    # Descrição
    descricao = models.TextField()

    # Relacionamento
    # Projeto
    projeto = models.ForeignKey(Projeto)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['descricao']
        verbose_name = 'objetivo'
        verbose_name_plural = 'objetivos'

    def __str__(self):
        return 'OE%d: %s' % (self.numero, self.descricao)
