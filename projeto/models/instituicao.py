from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
from django.contrib.auth.models import User
from localflavor.br.br_states import STATE_CHOICES

#
# Instituicão
#


class Instituicao(models.Model):

    sigla = models.CharField(max_length=256, validators=[
                             MinLengthValidator(2)])
    nome = models.CharField(max_length=256, validators=[
                            MinLengthValidator(5)])
    site = models.CharField(max_length=128, validators=[
                            MinLengthValidator(5)], blank=True)
    email = models.CharField(max_length=256, validators=[
                             EmailValidator()], blank=True)
    endereco = models.CharField(max_length=256, validators=[
                                MinLengthValidator(2)], blank=True)
    cidade = models.CharField(max_length=256, validators=[
                              MinLengthValidator(2)], blank=True)
    descricao = models.TextField(max_length=512, validators=[
                                 MinLengthValidator(10)], blank=True)
    cnpj = models.CharField(max_length=14, blank=True)
    telefone = models.CharField(max_length=16, blank=True)
    estado = models.CharField(max_length=16, choices=STATE_CHOICES, blank=True)
    cep = models.CharField(max_length=9, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['sigla']
        verbose_name = 'instituição'
        verbose_name_plural = 'instituições'

    def get_detail_url(self):
        return u"/instituicao/detail/%i" % self.id

    def get_update_url(self):
        return u"/instituicao/update/%i" % self.id

    def get_delete_url(self):
        return u"/instituicao/delete/%i" % self.id

    def __str__(self):
        return self.nome
