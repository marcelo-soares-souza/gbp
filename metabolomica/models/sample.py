from django.contrib.auth.models import User
from django.db import models

from metabolomica.models.database import Database
from metabolomica.models.species import Species

from projeto.models.template import TemplateModelMixin


class Sample(models.Model, TemplateModelMixin):

    database = models.ForeignKey(Database, null=True, blank=True, on_delete=models.SET_NULL)
    lab_code = models.CharField(max_length=64)
    replicate = models.CharField(max_length=64, blank=True)
    species = models.ForeignKey(Species, null=True, blank=True, on_delete=models.SET_NULL)
    bio_sample = models.CharField(max_length=64, blank=True)

    # Generic Data
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['lab_code']
        verbose_name = 'sample'
        verbose_name_plural = 'samples'

    def __str__(self):
        return '%s' % (self.lab_code)
