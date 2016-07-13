from django import forms

from sequenciamento.models import Contrato


class ContratoForm(forms.ModelForm):

    class Meta:
        model = Contrato
        fields = ('projeto', 'empresa_executora', 'status_contrato', 'status_pagamento', 'data_contratacao', 'status_cgen', 'ttm', 'contato_gestor', 'codigo_pedido_gestor', 'objetivo', 'descricao')

        labels = {
            'projeto': 'Projeto',
            'empresa_executora': 'Empresa Executora',
            'status_contrato': 'Status do Contrato',
            'status_pagamento': 'Status do Pagamento',
            'data_contratacao': 'Data de Contratação',
            'status_cgen': 'Status no CGEN',
            'ttm': 'TTM',
            'contato_gestor': 'Contato do Gestor',
            'codigo_pedido_gestor': 'Código do Pedido do Gestor',
            'objetivo': 'Objetivo',
            'descricao': 'Descrição'
        }
