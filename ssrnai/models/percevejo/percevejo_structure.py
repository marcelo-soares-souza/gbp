from ssrnai.models.organisms import Organisms
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information
from ssrnai.models.percevejo.percevejo_dsrna_information import Percevejo_Dsrna_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Percevejo_Structure(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Percevejo_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    dsrna = models.ForeignKey(Percevejo_Dsrna_Information("dsrna_id"), null=True, blank=True, on_delete=models.SET_NULL)
    mismatch = models.IntegerField(("mismatch"))
    match = models.IntegerField(("match"))
    composition = models.TextField(("composition"))
    classification= models.CharField("classification", max_length=50)
    interaction_energy= models.FloatField("interaction_energy", max_length=50)
    figure= models.CharField("figure", max_length=500)

    class Meta:
        ordering = ['id']
        verbose_name = 'dsrna'
        verbose_name_plural = 'dsrnas'

    def __str__(self):
        return '%s' % (self.dsrna_name)
