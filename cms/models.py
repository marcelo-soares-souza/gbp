from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from projeto.models.template import TemplateModelMixin


class Pagina(models.Model, TemplateModelMixin):

    titulo = models.CharField(max_length=256, validators=[MinLengthValidator(5)])
    texto = models.TextField(blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['titulo']
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'

    def __str__(self):
        return self.titulo
