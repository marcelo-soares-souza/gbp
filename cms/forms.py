from django import forms
from django.forms import Textarea, TextInput
from ckeditor.widgets import CKEditorWidget

from .models import Pagina


class PaginaForm(forms.ModelForm):
    texto = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Pagina
        fields = ('titulo', 'texto')

