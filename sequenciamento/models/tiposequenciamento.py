from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class TipoSequenciamento(models.Model):
    nome = models.CharField(validators=[MinLengthValidator(5)],
                            max_length=256)

    descricao = models.TextField(null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'tiposequenciamento'
        verbose_name_plural = 'tiposequenciamentos'

    def get_detail_url(self):
        return u"/tiposequenciamento/detail/%i" % self.id

    def get_update_url(self):
        return u"/tiposequenciamento/update/%i" % self.id

    def get_delete_url(self):
        return u"/tiposequenciamento/delete/%i" % self.id

    def __str__(self):
        return '%s' % self.nome
