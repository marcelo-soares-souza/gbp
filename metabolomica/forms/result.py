from forms import Forms

from metabolomica.models import Result

class ResultForm(forms.ModelForm):

    class Meta:

        model = 'Result'
        fields = (
             'sample_code',
             'experimental_condition',
             'equip_mode' 
             )
       
        labels = {
            'sample_code' = 'Sample Code',
            'experimental_condition' = 'Experimental Condition',
            'equip_mode' = 'Equipment Mode'
        }
