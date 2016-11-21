from django import forms

from metabolomica.models import Sample


class SampleForm(forms.ModelForm):

    class Meta:
        model = Sample
        fields = (
            'name',
            'lab_code',
            'species',
            'bio_sample',
            'criado_por')

        labels = {
            'name': 'Replicates',
            'lab_code': 'Lab Code',
            'species': 'Species',
            'bio_sample': 'Biological Sample',
            'criado_por': 'User'
        }
