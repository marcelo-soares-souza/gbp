from ssrnai.models.organisms import Organisms
from django.db import models
from projeto.models.template import TemplateModelMixin

class Conyza_expression_description(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    expression = models.CharField(("expression_id"), max_length=50)
    treatment = models.CharField(("treatment"), max_length=400)
    ncbi_id = models.CharField(("ncbi_id"), max_length=150)
    condition_description = models.TextField(("condition_description"))


    class Meta:
        ordering = ['id']
        verbose_name = 'expression_description'
        verbose_name_plural = 'expression_descriptions'

    def __str__(self):
        return '%s' % (self.expression)
