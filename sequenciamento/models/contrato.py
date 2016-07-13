from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from projeto.models.projeto import Projeto
from projeto.models.template import TemplateModelMixin


class Contrato(models.Model, TemplateModelMixin):
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

    STATUS_CGEN = (
        ('TTM - Preparado', 'TTM - Preparado'),
        ('TTM - Não Preparado', 'TTM - Não Preparado')
    )

    projeto = models.ForeignKey(Projeto)
    objetivo = models.TextField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    status_contrato = models.CharField(max_length=64, choices=STATUS_CONTRATO, null=True, blank=True)
    status_pagamento = models.CharField(max_length=64, choices=STATUS_PAGAMENTO, null=True, blank=True)
    empresa_executora = models.CharField(max_length=256, null=True, blank=True)
    data_contratacao = models.DateField(null=True, blank=True, default=timezone.now)
    status_cgen = models.CharField(max_length=64, choices=STATUS_CGEN, null=True, blank=True)
    ttm = models.CharField(max_length=256, null=True, blank=True)
    contato_gestor = models.CharField(max_length=256, null=True, blank=True)
    codigo_pedido_gestor = models.CharField(max_length=256, null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['projeto']
        verbose_name = 'contrato'
        verbose_name_plural = 'contratos'

    def __str__(self):
        if self.data_contratacao:
            return '%s - %s - %s' % (self.projeto, self.data_contratacao.strftime('%d/%m/%Y'), self.empresa_executora)
        else:
            return '%s - %s' % (self.projeto, self.empresa_executora)
