from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from projeto.models.projeto import Projeto
from projeto.models.template import TemplateModelMixin
from sequenciamento.models.tiposequenciamento import TipoSequenciamento


class Sequenciamento(models.Model, TemplateModelMixin):
    STATUS_CONTRATO = (
        ('Contratado', 'Contratado'),
        ('Em Contratação', 'Em Contratação'),
        ('Em Cotação', 'Em Cotação'),
        ('Finalizado', 'Finalizado')
    )

    STATUS_PAGAMENTO = (
        ('Aviso de Fornecimento', 'Aviso de Fornecimento'),
        ('Atencipação', 'Atencipação'),
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago')
    )

    PRIORIDADE = (
        ('Normal', 'Normal'),
        ('Urgente', 'Urgente')
    )

    STATUS_CGEN = (
        ('TTM - Preparado', 'TTM - Preparado'),
        ('TTM - Não Preparado', 'TTM - Não Preparado')
    )

    projeto = models.ForeignKey(Projeto)
    tipo_sequenciamento = models.ForeignKey(TipoSequenciamento)
    responsavel = models.ForeignKey(
        User, null=True, blank=True, related_name='responsavel_sequenciamento')

    objetivo = models.TextField(null=True, blank=True)
    material_biologico = models.CharField(
        validators=[MinLengthValidator(5)], max_length=256)
    descricao_material_biologico = models.TextField(null=True, blank=True)
    numero_amostras = models.IntegerField(null=True, blank=True, default=0)
    status_contrato = models.CharField(
        max_length=64, choices=STATUS_CONTRATO, null=True, blank=True)
    status_pagamento = models.CharField(
        max_length=64, choices=STATUS_PAGAMENTO, null=True, blank=True)
    prioridade = models.CharField(
        max_length=64, choices=PRIORIDADE, default='Normal')
    empresa_executora = models.CharField(max_length=256, null=True, blank=True)
    data_contratacao = models.DateField(null=True, blank=True)
    detalhamento_material = models.TextField(null=True, blank=True)
    status_cgen = models.CharField(
        max_length=64, choices=STATUS_CGEN, null=True, blank=True)
    ttm = models.CharField(max_length=256, null=True, blank=True)
    contato_gestor = models.CharField(max_length=256, null=True, blank=True)
    codigo_pedido_gestor = models.CharField(
        max_length=256, null=True, blank=True)

    colaborador = models.ManyToManyField(
        User, blank=True, related_name='colaborador_sequenciamento')

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['material_biologico']
        verbose_name = 'sequenciamento'
        verbose_name_plural = 'sequenciamentos'

    def __str__(self):
        return '%s' % self.material_biologico
