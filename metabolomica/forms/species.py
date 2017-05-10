from django import forms

from metabolomica.models import Species


class SpeciesForm(forms.ModelForm):

    class Meta:
        model = Species
        fields = (
                'name',
                'scientific_name',
                'strain',
                'criado_por')

        labels = {
                'name': 'Name',
                'scientific_name': 'Scientific Name',
                'strain': 'Strain',
                'criado_por': 'User'
        }

        widgets = {
            'strain': forms.TextInput(
                attrs = {'placeholder':
                'Strain/Cultivar/Variety'}
            )
        }
