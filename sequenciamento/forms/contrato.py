from django import forms

from sequenciamento.models import Contrato


class ContratoForm(forms.ModelForm):

    class Meta:
        model = Contrato
        fields = ('projeto', 'empresa_executora')

        labels = {
            'projeto': 'Projeto',
            'empresa_executora': 'Empresa Executora'
        }
