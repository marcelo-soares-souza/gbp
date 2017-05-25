from django import forms

from metabolomica.models import Analytical


class AnalyticalForm(forms.ModelForm):

    class Meta:
        model = Analytical
        fields = ('name',
                  'description')

        labels = {
            'name': 'Name',
            'description': 'Description'
        }
