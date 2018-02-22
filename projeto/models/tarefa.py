from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from projeto.models.atividade import Atividade
from projeto.models.planoacao import PlanoAcao
from projeto.models.projeto import Projeto
from projeto.models.template import TemplateModelMixin


#
# Tarefas
#


class Tarefa(models.Model, TemplateModelMixin):

    # Atributos
    numero = models.PositiveIntegerField(blank=True, default=1)
    nome = models.CharField(max_length=100, validators=[
                            MinLengthValidator(2)], blank=True)
    indicador_fisico = models.CharField(max_length=32, validators=[
                                        MinLengthValidator(2)], blank=True)
    peso_atividade = models.PositiveIntegerField(blank=True, default=1)

    # Relacionamentos
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

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
        User, null=True, blank=True, related_name='responsavel_tarefa', on_delete=models.CASCADE)
    colaborador = models.ManyToManyField(
        User, blank=True, related_name='colaborador_tarefa')

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nome']
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'

    def __str__(self):
        return 'TF%d: %s' % (self.numero, self.nome)
