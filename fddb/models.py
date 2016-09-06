from django.contrib.auth.models import User
from django.db import models

from projeto.models.template import TemplateModelMixin


class Fddb(models.Model, TemplateModelMixin):

    ORGANISMOS = (
        ('BR1', 'BR174'),
        ('COA', 'Coari'),
        ('MAN', 'Manicoré'),
    )

    organismo = models.CharField(max_length=64, choices=ORGANISMOS, default='BR1')
    folha = models.CharField(max_length=4)
    complemento = models.CharField(max_length=16, null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['organismo']
        verbose_name = 'fddb'
        verbose_name_plural = 'fddbs'

    def __str__(self):
        return "%s" % (self.complemento)
