from django.db import models

from projeto.model.template import TemplateModelMixin

class Equipment(models.Model, TemplateModelMixin):

    name = model.CharField(max_length=64)
    description = model.TextField(null=True, blank=True)

    # Generic Data
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)
    
    Class meta:

        ordering = ['name']
        name_verbose = 'equipment'
        name_verbose_plural = 'equipments'
    
    def __str__(self):
        return '%' % (self.name)
