from django import forms

from metabolomica.models import Experiment


class ExperimentForm(forms.ModelForm):

    class Meta:
        model = Experiment
        fields = ('name', 'project', 'description')

        labels = {
            'name': 'Name',
            'project': 'Project',
            'description': 'Description'
        }
