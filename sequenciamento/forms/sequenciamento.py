
from django import forms
from django.forms import ModelForm, Textarea, TextInput
from sequenciamento.models import Sequenciamento
from localflavor.br.forms import BRCNPJField, BRPhoneNumberField, BRZipCodeField, BRStateSelect


class SequenciamentoForm(forms.ModelForm):

    class Meta:
        model = Sequenciamento
        fields = ('projeto', 'material_biologico', 'tipo_sequenciamento',
                  'responsavel', 'objetivo', 'descricao_material_biologico',
                  'numero_amostras', 'status_contrato', 'status_pagamento',
                  'prioridade', 'empresa_executora', 'data_contratacao',
                  'detalhamento_material', 'status_cgen', 'ttm',
                  'contato_gestor', 'codigo_pedido_gestor', 'colaborador')

        labels = {
            'material_biologico': 'Matérial Biológico',
            'tipo_sequenciamento': 'Tipo de Sequenciamento',
            'responsavel': 'Responsável',
            'objetivo': 'Objetivo',
            'descricao_material_biologico': 'Descrição do Matérial Biológico',
            'numero_amostras': 'Número de Amostras',
            'status_contrato': 'Status do Contrato',
            'status_pagamento': 'Status do Pagamento',
            'prioridade': 'Prioridade',
            'empresa_executora': 'Empresa Executora',
            'data_contratacao': 'Data de Contratação',
            'detalhamento_material': 'Detalhamento do Material',
            'status_cgen': 'Status no CGEN',
            'ttm': 'TTM',
            'contato_gestor': 'Contato do Gestor',
            'codigo_pedido_gestor': 'Código do Pedido do Gestor',
            'colaborador': 'Colaboradores'
        }
