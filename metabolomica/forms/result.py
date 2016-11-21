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
             'equip_mode',
             'parameters_lc_ms',
             'extr_method',
             'lc_raw_data',
             'ms_raw_data',
             'raw_data',
             'process_data'
        )

        labels = {
            'name': 'Name',
            'sample': 'Sample',
            'experimental_condition': 'Experimental Condition',
            'equipment': 'Equipment',
            'analytical_method': 'Analytical Method',
            'equip_mode': 'MS Mode',
            'extr_method': 'Extraction Method',
            'parameters_lc_ms': 'Analytical Parameters - LC and MS',
            'lc_raw_data': 'Analytical Method - LC Raw Data',
            'ms_raw_data': 'Analytical Method - MS Raw Data',
            'raw_data': 'Result Raw Data',
            'process_data': 'Processed Data'
        }
