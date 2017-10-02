from django import forms

from metabolomica.models import MsMode


class MsModeForm(forms.ModelForm):

    class Meta:
        model = MsMode
        fields = (
            'name',
            'description'
        )

        labels = {
            'name': 'MS Mode',
            'description': 'Description'
        }
