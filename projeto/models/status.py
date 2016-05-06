from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

#
# Status do Projeto
#


class Status(models.Model):

    nome = models.CharField(max_length=32, validators=[
                            MinLengthValidator(2)], blank=True)
    descricao = models.TextField(null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'status'
        verbose_name_plural = 'status'

    def get_detail_url(self):
        return u"/status/detail/%i" % self.id

    def get_delete_url(self):
        return u"/status/delete/%i" % self.id

    def __str__(self):
        return self.nome
