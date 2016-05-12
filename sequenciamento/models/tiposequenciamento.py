from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from projeto.models.template import TemplateModelMixin


class TipoSequenciamento(models.Model, TemplateModelMixin):
    nome = models.CharField(validators=[MinLengthValidator(5)],
                            max_length=256)

    descricao = models.TextField(null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'tiposequenciamento'
        verbose_name_plural = 'tiposequenciamentos'

    def __str__(self):
        return '%s' % self.nome
