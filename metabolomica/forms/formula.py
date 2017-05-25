from django import forms

from metabolomica.models import Formula


class FormulaForm(forms.ModelForm):

    class Meta:
        model = Formula
        fields = (
            'common_name',
            'chemical_formula',
            'criado_por')

        labels = {
            'common_name': 'Common Name',
            'chemical_formula': 'Chemical Formula',
            'criado_por': 'User'
        }
