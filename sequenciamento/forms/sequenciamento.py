from django import forms

from sequenciamento.models import Sequenciamento


class SequenciamentoForm(forms.ModelForm):

    class Meta:
        model = Sequenciamento
        fields = ('contrato', 'material_biologico', 'tipo_sequenciamento',
                  'responsavel', 'finalidade', 'descricao_material_biologico',
                  'numero_amostras', 'prioridade', 'detalhamento_material', 'colaborador')

        labels = {
            'contrato': 'Contrato',
            'material_biologico': 'Matérial Biológico',
            'tipo_sequenciamento': 'Tipo de Sequenciamento',
            'responsavel': 'Responsável',
            'finalidade': 'Finalidade',
            'descricao_material_biologico': 'Descrição do Matérial Biológico',
            'numero_amostras': 'Número de Amostras',
            'prioridade': 'Prioridade',
            'detalhamento_material': 'Detalhamento do Material',
            'colaborador': 'Colaboradores'
        }
