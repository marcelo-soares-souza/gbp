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
            'analytical_method',
            'lc_method',
            'ms_method',
            'parameters',
            'sample_preparation',
            'raw_data',
            'processed_data',
            'csv',
            'image',
        )

        labels = {
            'name': 'Result title',
            'sample': 'Sample',
            'experimental_condition': 'Experimental Condition',
            'equipment': 'Equipments',
            'analytical_method': 'Analytical Method',
            'lc_method': 'LC Method (Instrument)',
            'ms_method': 'MS Method (Instrument)',
            'parameters': 'Parameters',
            'sample_preparation': 'Sample Preparation',
            'raw_data': 'Raw Data',
            'processed_data': 'Processed Data',
            'csv': 'CSV Upload',
            'image': 'Image Upload',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Result title'}
            )
        }
