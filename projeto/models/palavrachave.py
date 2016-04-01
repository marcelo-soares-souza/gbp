from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

#
# Palavras chaves dos projetos
#

class PalavraChave(models.Model):
    
    palavra = models.CharField(max_length=32, validators=[MinLengthValidator(2)], blank=True)
    descricao = models.CharField(max_length=256, validators=[MinLengthValidator(3)], null=True, blank=True)
    
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['palavra']
        verbose_name = 'palavra chave'
        verbose_name_plural = 'palavras chave'

    def get_palavrachave_detail_url(self):
        return u"/palavrachave/detail/%i" % self.id
    
    def get_palavrachave_update_url(self):
        return u"/palavrachave/update/%i" % self.id
        
    def get_palavrachave_delete_url(self):
        return u"/palavrachave/delete/%i" % self.id

    def __str__(self):
        return self.palavra
