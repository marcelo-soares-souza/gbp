from django import forms

from sequenciamento.models import TipoSequenciamento


class TipoSequenciamentoForm(forms.ModelForm):

    class Meta:
        model = TipoSequenciamento
        fields = ('nome', 'descricao')

        widgets = {
            'descricao': forms.Textarea(attrs={'cols': '5', 'rows': '5'}),
        }

        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
        }
