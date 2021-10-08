from ssrnai.models.organisms import Organisms
from ssrnai.models.capim.capim_gene_information import Capim_Gene_Information
from ssrnai.models.capim.capim_dsrna_information import Capim_Dsrna_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Capim_Dicer(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Capim_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    dsrna = models.ForeignKey(Capim_Dsrna_Information("dsrna_id"), null=True, blank=True, on_delete=models.SET_NULL)
    sirna_number = models.IntegerField("sirna_number")
    coverage = models.IntegerField(("coverage"))
    location = models.TextField(("location"))


    class Meta:
        ordering = ['id']
        verbose_name = 'dicer'
        verbose_name_plural = 'dicers'

    def __str__(self):
        return '%s' % (self.id)
