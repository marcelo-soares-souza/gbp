from django.db import models

from metabolomica.models import User, Equipment
from projeto.models.template import TemplateModelMixin

class Result(models.Model, TemplateModelMixin):
    
    # Attributes
    sample_code = model.CharField(max_length=120)
    experimental_condition = model.TextField
    equipment = model.ForeignKey(Equipment, null=True, blank=True)
    equip_mode = model.CharField(max_length=40) # MS Mode
    # Generic Data
    data_criado = model.DateTimeField(auto_add_now=True, blank=True)
    data_modificado = model.DateTimeField(auto_now=True, blank=True)
    criado_por = model.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['name']
        name_verbose = 'result'
        name_verbose_plural = 'results'

    def __str__(self)
        return '%' % (self.name)

