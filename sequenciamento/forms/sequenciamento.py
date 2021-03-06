from django import forms

from sequenciamento.models import Sequenciamento


class SequenciamentoForm(forms.ModelForm):

    class Meta:
        model = Sequenciamento
        fields = ('numero', 'contrato', 'material_biologico', 'tipo_sequenciamento',
                  'responsavel', 'finalidade', 'descricao_material_biologico',
                  'numero_amostras', 'prioridade', 'detalhamento_material', 'colaborador')

        labels = {
            'numero': 'Número',
            'contrato': 'Contrato',
            'material_biologico': 'Material Biológico',
            'tipo_sequenciamento': 'Tipo de Sequenciamento',
            'responsavel': 'Responsável',
            'finalidade': 'Finalidade',
            'descricao_material_biologico': 'Descrição do Material Biológico',
            'numero_amostras': 'Número de Amostras',
            'prioridade': 'Prioridade',
            'detalhamento_material': 'Detalhamento do Material',
            'colaborador': 'Colaboradores'
        }
