from django import forms

from metabolomica.models import Database


class DatabaseForm(forms.ModelForm):

    class Meta:
        model = Database
        fields = (
            'name',
            'description')

        labels = {
            'name': 'Name',
            'description': 'Description',
        }
