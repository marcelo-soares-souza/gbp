from django.contrib.auth.models import User
from django.db import models

from projeto.models.template import TemplateModelMixin


class Equipment(models.Model, TemplateModelMixin):

    name = models.CharField(max_length=64, blank=True)

    # Generic Data
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'equipment'
        verbose_name_plural = 'equipments'

    def __str__(self):
        return '%s' % (self.name)
