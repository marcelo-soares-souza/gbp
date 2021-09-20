from django.contrib.auth.models import User
from django.db import models

from projeto.models.template import TemplateModelMixin


class Formula(models.Model, TemplateModelMixin):

    common_name = models.CharField(max_length=150)
    chemical_formula = models.CharField(max_length=150)

    # Generic Data
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['common_name']
        verbose_name = 'formula'
        verbose_name_plural = 'formulae'

    def __str__(self):
        return '%s' % (self.common_name)
