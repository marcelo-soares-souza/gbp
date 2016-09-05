from django.contrib.auth.models import User
from django.db import models

from projeto.models.template import TemplateModelMixin


class Sample(models.Model, TemplateModelMixin):

    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)

    # Generic Data
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'sample'
        verbose_name_plural = 'samples'

    def __str__(self):
        return '%s' % (self.name)
