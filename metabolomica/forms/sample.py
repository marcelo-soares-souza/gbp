from django import forms

from metabolomica.models import Sample


class SampleForm(forms.ModelForm):

    class Meta:
        model = Sample
        fields = ('name', 'description')

        labels = {
            'name': 'Name',
            'description': 'Description'
        }
