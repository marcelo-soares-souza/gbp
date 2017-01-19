from django import forms

from metabolomica.models import Approach


class ApproachForm(forms.ModelForm):

    class Meta:
        model = Approach
        fields = ('project',
                  'name',
                  'description')

        labels = {
            'project': 'Project',
            'name': 'Name',
            'description': 'Description'
        }
