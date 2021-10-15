from ssrnai.models.organisms import Organisms
from ssrnai.models.capim.capim_gene_information import Capim_Gene_Information
from ssrnai.models.capim.capim_dsrna_information import Capim_Dsrna_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Capim_Structure(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Capim_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    dsrna = models.ForeignKey(Capim_Dsrna_Information("dsrna_id"), null=True, blank=True, on_delete=models.SET_NULL)
    mismatch = models.IntegerField("mismatch", null=True, blank=True)
    match = models.IntegerField("match", null=True, blank=True)
    composition = models.TextField("composition", null=True, blank=True)
    classification= models.CharField("classification", max_length=50, null=True)
    interaction_energy= models.FloatField("interaction_energy", max_length=50, null=True, blank=True)
    figure= models.CharField("figure", max_length=500, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'structure'
        verbose_name_plural = 'structures'

    def __str__(self):
        return '%s' % (self.dsrna_name)
