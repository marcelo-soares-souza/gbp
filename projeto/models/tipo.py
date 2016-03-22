from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

#
# Tipos de Projetos
#

class Tipo(models.Model):

    sigla = models.CharField(max_length=256, validators=[MinLengthValidator(3)], blank=True)
    descricao = models.TextField(null=True, blank=True)
    
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['sigla']
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'

    def get_tipo_detail_url(self):
        return u"/tipo/detail/%i" % self.id

    def get_tipo_update_url(self):
        return u"/tipo/update/%i" % self.id

    def get_tipo_delete_url(self):
        return u"/tipo/delete/%i" % self.id

    def __str__(self):
        return self.sigla
