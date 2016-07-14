from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from projeto.models.template import TemplateModelMixin
from sequenciamento.models.contrato import Contrato
from sequenciamento.models.tiposequenciamento import TipoSequenciamento


class Sequenciamento(models.Model, TemplateModelMixin):
    PRIORIDADE = (
        ('Normal', 'Normal'),
        ('Urgente', 'Urgente')
    )

    contrato = models.ForeignKey(Contrato)
    tipo_sequenciamento = models.ForeignKey(TipoSequenciamento)
    responsavel = models.ForeignKey(User, null=True, blank=True, related_name='responsavel_sequenciamento')

    finalidade = models.TextField(null=True, blank=True)
    material_biologico = models.CharField(validators=[MinLengthValidator(5)], max_length=256)
    descricao_material_biologico = models.TextField(null=True, blank=True)
    numero_amostras = models.IntegerField(null=True, blank=True, default=0)
    prioridade = models.CharField(max_length=64, choices=PRIORIDADE, default='Normal')
    detalhamento_material = models.TextField(null=True, blank=True)

    colaborador = models.ManyToManyField(User, blank=True, related_name='colaborador_sequenciamento')

    numero = models.PositiveIntegerField(unique=True, null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['material_biologico']
        verbose_name = 'sequenciamento'
        verbose_name_plural = 'sequenciamentos'

    def __str__(self):
        return '%s - %s - %s' % (self.tipo_sequenciamento, self.numero_amostras, self.material_biologico)
