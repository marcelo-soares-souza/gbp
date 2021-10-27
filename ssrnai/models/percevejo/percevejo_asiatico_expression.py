from django.db.models.fields import FloatField
from ssrnai.models.organisms import Organisms
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Percevejo_Asiatico_Expression(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Percevejo_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    halys_whole1 = FloatField(("halys_whole1"), null=True, blank=True)
    halys_whole2 = FloatField(("halys_whole2"), null=True, blank=True)
    halys_antennae1 = FloatField(("halys_antennae1"), null=True, blank=True)
    halys_gut = FloatField(("halys_gut"), null=True, blank=True)
    halys_antennae2 = FloatField(("halys_antennae2"), null=True, blank=True)
    halys_antennae3 = FloatField(("halys_antennae3"), null=True, blank=True)
    halys_salivary1 = FloatField(("halys_salivary1"), null=True, blank=True)
    halys_salivary2 = FloatField(("halys_salivary2"), null=True, blank=True)
    halys_salivary3 = FloatField(("halys_salivary3"), null=True, blank=True)
    halys_salivary4 = FloatField(("halys_salivary4"), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'halys_expression'
        verbose_name_plural = 'halys_expressions'

    def __str__(self):
        return '%s' % (self.id)
