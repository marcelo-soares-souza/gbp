from django import forms

from ssrnai.models import Organisms


class OrganismForm(forms.ModelForm):

    class Meta:
        model = Organisms
        fields = (
            'organism_name',)

        labels = {
            'organism': 'Escolha o organismo:'
        }
