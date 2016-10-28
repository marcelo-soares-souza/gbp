from django.contrib.auth.models import User
from django.db import models

from metabolomica.models import Equipment, Sample

from projeto.models.template import TemplateModelMixin


class Result(models.Model, TemplateModelMixin):

    name = models.CharField(max_length=120)
    sample = models.ForeignKey(Sample, null=True, blank=True)  # Sample Code
    experimental_condition = models.TextField(null=True, blank=True)
    equipment = models.ForeignKey(Equipment, null=True, blank=True)
    equip_mode = models.CharField(max_length=40)  # MS Mode

    # Generic Data
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'result'
        verbose_name_plural = 'results'

    def __str__(self):
        return '%s' % (self.name)
