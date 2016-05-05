from django.contrib import admin

from .models import Tipo
from .models import Status

admin.site.register(Tipo)
admin.site.register(Status)
