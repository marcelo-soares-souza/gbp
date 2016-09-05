from django import forms

from .models import Citometria


class CitometriaForm(forms.ModelForm):

    class Meta:
        model = Citometria
        fields = ('organismo', 'folha')
