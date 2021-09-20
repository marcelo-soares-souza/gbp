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
            'bio_sample')

        labels = {
            'database': 'Database',
            'lab_code': 'Sample Lab Code',
            'replicate': 'Replicate',
            'species': 'Species',
            'bio_sample': 'Biological Sample'
        }

        widgets = {
            'replicate': forms.TextInput(
                attrs={'placeholder': 'B-biological/T-technical/A-analytical'}
            )
        }
