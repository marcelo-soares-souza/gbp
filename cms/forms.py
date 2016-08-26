from django import forms
from django.forms import Textarea, TextInput

from .models import Pagina


class PaginaForm(forms.ModelForm):

    class Meta:
        model = Pagina
        fields = ('titulo', 'texto')

