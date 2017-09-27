from django.contrib.auth.models import User
from django.db import models

from metabolomica.models.analytical import Analytical
from metabolomica.models.equipment import Equipment
from metabolomica.models.sample import Sample

from projeto.models.template import TemplateModelMixin


class Result(models.Model, TemplateModelMixin):

    name = models.CharField(max_length=120)
    sample = models.ForeignKey(Sample, null=True, blank=True, related_name='result_sample', on_delete=models.CASCADE)
    experimental_condition = models.TextField(blank=True)
    equipment = models.ManyToManyField(Equipment, blank=True, related_name='result_equipment')
    analytical_method = models.ForeignKey(Analytical, blank=True, null=True, related_name='result_analytical', on_delete=models.SET_NULL)
    equip_mode = models.CharField(max_length=40, null=True, blank=True)  # MS Mode
    raw_data = models.FileField(upload_to='bmdb/raw/%Y/%m/%d/', null=True, blank=True)  # Result raw data
    image = models.ImageField(upload_to='bmdb/raw/%Y/%m/%d/', height_field=None, width_field=None, max_length=None, null=True, blank=True)

    # Generic Data
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']
        verbose_name = 'result'
        verbose_name_plural = 'results'

    def __str__(self):
        return '%s' % (self.name)
