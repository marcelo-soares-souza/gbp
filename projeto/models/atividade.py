from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey

from projeto.models.planoacao import PlanoAcao
from projeto.models.projeto import Projeto
from projeto.models.template import TemplateModelMixin


#
# Atividade
#


class Atividade(models.Model, TemplateModelMixin):

    # Atributos
    numero = models.PositiveIntegerField(blank=True, default=1)
    nome = models.CharField(max_length=100, validators=[
                            MinLengthValidator(2)], blank=True)
    indicador_fisico = models.CharField(max_length=32, validators=[
                                        MinLengthValidator(2)], blank=True)
    peso_planoacao = models.PositiveIntegerField(blank=True, default=1)
    data_inicio = models.DateField(blank=True, default=timezone.now)
    data_fim = models.DateField(blank=True, default=timezone.now)

    # Relacionamentos
    projeto = models.ForeignKey(Projeto)

    planoacao = ChainedForeignKey(
        PlanoAcao,
        chained_field="projeto",
        chained_model_field="projeto",
        show_all=False,
        auto_choose=False
    )

    responsavel = models.ForeignKey(
        User, null=True, blank=True, related_name='responsavel_atividade')
    colaborador = models.ManyToManyField(
        User, blank=True, related_name='colaborador_atividade')

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'atividade'
        verbose_name_plural = 'atividades'

    def __str__(self):
        return 'AT%d: %s' % (self.numero, self.nome)
