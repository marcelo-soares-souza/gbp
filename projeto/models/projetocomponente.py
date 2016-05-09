from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

from projeto.models.template import TemplateModelMixin
from projeto.models.projeto import Projeto


#
# Projeto Componente
#

class ProjetoComponente(models.Model, TemplateModelMixin):

    numero = models.PositiveIntegerField(default=1)
    nome = models.CharField(max_length=256, validators=[MinLengthValidator(5)])
    responsavel = models.ForeignKey(
        User, null=True, blank=True, related_name='responsavel')
    projeto = models.ForeignKey(Projeto)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'projeto componente'
        verbose_name_plural = 'projetos componentees'

    def __str__(self):
        return 'PC%d: %s' % (self.numero, self.nome)
