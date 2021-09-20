from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Pagina


class PaginaForm(forms.ModelForm):
    texto = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Pagina
        fields = ('titulo', 'texto')
