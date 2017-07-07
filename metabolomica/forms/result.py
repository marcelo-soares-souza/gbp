from django import forms

from metabolomica.models import Result


class ResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = (
             'name',
             'sample',
             'experimental_condition',
             'equipment',
             'equip_mode',
             'analytical_method',
             'raw_data',
        )

        labels = {
            'name': 'Result title',
            'sample': 'Sample',
            'experimental_condition': 'Experimental Condition',
            'equipment': 'Equipments',
            'equip_mode': 'MS Mode',
            'analytical_method': 'Analytical Method',
            'raw_data': 'File Upload',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Result title'}
            )
        }
