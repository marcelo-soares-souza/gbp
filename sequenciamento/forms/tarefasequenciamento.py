from django import forms

from sequenciamento.models import TarefaSequenciamento


class TarefaSequenciamentoForm(forms.ModelForm):

    class Meta:
        model = TarefaSequenciamento
        fields = ('sequenciamento', 'tarefa', 'status', 'responsavel', 'observacao')

        widgets = {
            'observacao': forms.Textarea(attrs={'cols': '5', 'rows': '5'}),
        }

        labels = {
            'sequenciamento': 'Sequenciamento',
            'tarefa': 'Tarefa',
            'status': 'Status',
            'responsavel': 'Responsável',
            'observacao': 'Observação',
        }
