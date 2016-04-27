from django.contrib import admin

from .models import Tipo
from .models import Status

# class ProjetoAdmin(admin.ModelAdmin):
#    list_display = ('sigla', )
#    list_filter = ['sigla']
#    search_fields = ['sigla']

admin.site.register(Tipo)
admin.site.register(Status)
