from django import forms

from metabolomica.models import Experiment


class ExperimentForm(forms.ModelForm):

    class Meta:
        model = Experiment
        fields = ('name', 'description')

        labels = {
            'name': 'Name',
            'description': 'Description'
        }
