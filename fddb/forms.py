from django import forms

from .models import Fddb


class FddbForm(forms.ModelForm):

    class Meta:
        model = Fddb
        fields = ('organismo', 'folha')
