from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

from projeto.models.projeto import Projeto
from projeto.models.planoacao import PlanoAcao
from projeto.models.atividade import Atividade

#
# Tarefas
#


class Tarefa(models.Model):

    # Atributos
    numero = models.PositiveIntegerField(blank=True)
    nome = models.CharField(max_length=100, validators=[
                            MinLengthValidator(2)], blank=True)
    indicador_fisico = models.CharField(max_length=32, validators=[
                                        MinLengthValidator(2)], blank=True)
    peso_atividade = models.PositiveIntegerField(blank=True)

    # Relacionamentos
    projeto = models.ForeignKey(Projeto, blank=True)

    planoacao = ChainedForeignKey(
        PlanoAcao,
        chained_field="projeto",
        chained_model_field="projeto",
        show_all=False,
        auto_choose=False
    )

    atividade = ChainedForeignKey(
        Atividade,
        chained_field="planoacao",
        chained_model_field="planoacao",
        show_all=False,
        auto_choose=False
    )

    responsavel = models.ForeignKey(
        User, null=True, blank=True, related_name='responsavel_tarefa')
    colaborador = models.ManyToManyField(
        User, blank=True, related_name='colaborador_tarefa')

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'

    def get_tarefa_detail_url(self):
        return u"/tarefa/detail/%i" % self.id

    def get_tarefa_update_url(self):
        return u"/tarefa/update/%i" % self.id

    def get_tarefa_delete_url(self):
        return u"/tarefa/delete/%i" % self.id

    def __str__(self):
        return 'TF%d: %s' % (self.numero, self.nome)
