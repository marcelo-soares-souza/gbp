
from django import forms
from django.forms import ModelForm, Textarea, TextInput
from sequenciamento.models import TipoSequenciamento
from localflavor.br.forms import BRCNPJField, BRPhoneNumberField, BRZipCodeField, BRStateSelect


class TipoSequenciamentoForm(forms.ModelForm):

    class Meta:
        model = TipoSequenciamento
        fields = ('nome', 'descricao')

        widgets = {
            'descricao': Textarea(attrs={'cols': '5', 'rows': '5'}),
        }

        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
        }
