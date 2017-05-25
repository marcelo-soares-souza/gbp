from django.contrib.auth.models import User
from django.db import models

from projeto.models.template import TemplateModelMixin


class Species(models.Model, TemplateModelMixin):

    name = models.CharField(max_length=64)
    scientific_name = models.CharField(max_length=150)
    strain = models.CharField(max_length=64, null=True, blank=True)  # Strain/Cultivar/Variety

    # Generic Data
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']
        verbose_name = 'species'
        verbose_name_plural = 'species'

    def __str__(self):
        return '%s' % (self.name)
