from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from projeto.models.template import TemplateModelMixin


class Citometria(models.Model, TemplateModelMixin):

    ORGANISMOS = (
        ('BR174', 'BR174'),
        ('COARI', 'Coari'),
        ('Manicoré', 'Manicoré'),
    )

    organismo = models.CharField(max_length=64, choices=ORGANISMOS, default='BR174')
    folha = models.CharField(max_length=4)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['organismo']
        verbose_name = 'citometria'
        verbose_name_plural = 'citometrias'

    def __str__(self):
        return self.organismo
