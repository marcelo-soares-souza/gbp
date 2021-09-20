from django import forms

from metabolomica.models import Projeto


class ProjectForm(forms.ModelForm):

    class Meta:

        model = Projeto
        fields = ('name', 'description')

        labels = {
            'name': 'Name',
            'description': 'Description'
        }
