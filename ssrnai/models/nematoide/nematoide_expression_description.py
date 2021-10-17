from ssrnai.models.organisms import Organisms
from django.db import models
from projeto.models.template import TemplateModelMixin

class Nematoide_expression_description(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    dataset = models.CharField(("dataset"), max_length=50, null=True, blank=True)
    expression = models.CharField(("expression_id"), max_length=50, null=True, blank=True)
    species = models.CharField(("species"), max_length=150, null=True, blank=True)
    stage = models.CharField(("stage"), max_length=100, null=True, blank=True)
    ncbi_id = models.CharField(("ncbi_id"), max_length=150, null=True, blank=True)
    condition_description = models.TextField(("condition_description"), null=True, blank=True)


    class Meta:
        ordering = ['id']
        verbose_name = 'expression_description'
        verbose_name_plural = 'expression_descriptions'

    def __str__(self):
        return '%s' % (self.expression)
