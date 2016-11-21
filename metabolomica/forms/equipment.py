from django import forms

from metabolomica.models import Equipment


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('name', 'system')

        labels = {
            'name': 'Name',
            'system': 'System',
        }
