from ssrnai.models.organisms import Organisms
from ssrnai.models.conyza.conyza_gene_information import Conyza_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Conyza_Network(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene1 = models.ForeignKey(Conyza_Gene_Information("gene_id"), related_name='gene1', null=True, blank=True, on_delete=models.SET_NULL)
    gene2 = models.ForeignKey(Conyza_Gene_Information("gene_id"), related_name='gene2', null=True, blank=True, on_delete=models.SET_NULL)
    correlation = models.FloatField(("correlation"))
    p_value = models.FloatField(("p_value"))
    group = models.CharField(("group"), max_length=100)


    class Meta:
        ordering = ['id']
        verbose_name = 'network'
        verbose_name_plural = 'networks'

    def __str__(self):
        return '%s' % (self.dsrna_name)