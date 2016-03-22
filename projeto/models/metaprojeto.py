from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedManyToManyField

from projeto.models.projeto import Projeto
from projeto.models.objetivo import Objetivo


#
# Objetivo de Projetos
#

class MetaProjeto(models.Model):

    numero = models.IntegerField(blank=True)
    nome = models.CharField(max_length=256, validators=[MinLengthValidator(5)], blank=True)
    projeto = models.ForeignKey(Projeto, null=True, blank=True)

    objetivo = ChainedManyToManyField(
        Objetivo,
        chained_field="projeto",
        chained_model_field="projeto",
    )

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'meta'
        verbose_name_plural = 'metas'

    def get_metaprojeto_detail_url(self):
        return u"/metaprojeto/detail/%i" % self.id

    def get_metaprojeto_update_url(self):
        return u"/metaprojeto/update/%i" % self.id

    def get_metaprojeto_delete_url(self):
        return u"/metaprojeto/delete/%i" % self.id

    def __str__(self):
        return 'MT%d: %s' % (self.numero, self.nome)
