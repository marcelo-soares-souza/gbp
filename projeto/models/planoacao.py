from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

from projeto.models.projeto import Projeto
from projeto.models.projetocomponente import ProjetoComponente
from projeto.models.resultado import Resultado
from projeto.models.template import TemplateModelMixin

from smart_selects.db_fields import ChainedManyToManyField


#
# Plano de Ação
#


class PlanoAcao(models.Model, TemplateModelMixin):

    # Atributos
    numero = models.PositiveIntegerField(default=1)
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    responsavel = models.ForeignKey(User, null=True, blank=True, related_name='responsavel_plano', on_delete=models.CASCADE)
    codigo_seg = models.CharField(max_length=32, validators=[
                                  MinLengthValidator(2)], blank=True)
    data_inicio = models.DateField(blank=True, default=timezone.now)
    data_fim = models.DateField(blank=True, default=timezone.now)

    # Relacionamentos
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    projeto_componente = models.ManyToManyField(ProjetoComponente, blank=True, related_name='projeto_componente')

    resultado = ChainedManyToManyField(
        Resultado,
        chained_field="projeto",
        chained_model_field="projeto",
        auto_choose=True,
    )

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nome']
        verbose_name = 'plano de ação'
        verbose_name_plural = 'planos de ação'

    def __str__(self):
        return 'PA%d: %s' % (self.numero, self.nome)
