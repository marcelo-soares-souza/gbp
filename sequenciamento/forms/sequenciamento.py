
from django import forms
from django.forms import ModelForm, Textarea, TextInput
from sequenciamento.models import Sequenciamento
from localflavor.br.forms import BRCNPJField, BRPhoneNumberField, BRZipCodeField, BRStateSelect


class SequenciamentoForm(forms.ModelForm):

    class Meta:
        model = Sequenciamento
        fields = ('projeto', 'material_biologico')

        labels = {
            'material_biologico': 'Matérial Biológico',
        }
