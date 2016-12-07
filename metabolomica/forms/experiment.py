from django import forms

from metabolomica.models import Experiment


class ExperimentForm(forms.ModelForm):

    class Meta:
        model = Experiment
        fields = ('project',
                  'name',
                  'description')

        labels = {
            'project': 'Project',
            'name': 'Name',
            'description': 'Description'
        }
