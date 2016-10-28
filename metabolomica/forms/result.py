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
             )

        labels = {
            'name': 'Name',
            'sample': 'Sample',
            'experimental_condition': 'Experimental Condition',
            'equipment': 'Equipment',
            'equip_mode': 'Equipment Mode',
        }
