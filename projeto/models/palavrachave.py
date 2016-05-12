from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from projeto.models.projeto import Projeto
from projeto.models.template import TemplateModelMixin


#
# Palavras chaves dos projetos
#


class PalavraChave(models.Model, TemplateModelMixin):

    projeto = models.ForeignKey(Projeto)

    palavra = models.CharField(max_length=32, validators=[
                               MinLengthValidator(2)])

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['palavra']
        verbose_name = 'palavra chave'
        verbose_name_plural = 'palavras chave'

    def __str__(self):
        return self.palavra
