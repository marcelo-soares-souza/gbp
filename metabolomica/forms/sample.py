from django import forms

from metabolomica.models import Sample


class SampleForm(forms.ModelForm):

    class Meta:
        model = Sample
        fields = (
            'database',
            'lab_code',
            'replicate',
            'species',
            'bio_sample',
            'criado_por')

        labels = {
            'database': 'Database',
            'lab_code': 'Sample Lab Code',
            'replicate': 'Replicate',
            'species': 'Species',
            'bio_sample': 'Biological Sample',
            'criado_por': 'User'
        }

        widgets = {
            'replicate': forms.TextInput(
                attrs={'placeholder': 'B-biological/T-technical/A-analytical'}
            )
        }
