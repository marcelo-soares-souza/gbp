from ssrnai.models.organisms import Organisms
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information
from ssrnai.models.percevejo.percevejo_dsrna_information import Percevejo_Dsrna_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Percevejo_Dicer(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Percevejo_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    dsrna = models.ForeignKey(Percevejo_Dsrna_Information("dsrna_id"), null=True, blank=True, on_delete=models.SET_NULL)
    sirna_number = models.IntegerField("sirna_number")
    coverage = models.IntegerField(("coverage"))
    location = models.TextField(("location"))


    class Meta:
        ordering = ['id']
        verbose_name = 'dicer'
        verbose_name_plural = 'dicers'

    def __str__(self):
        return '%s' % (self.id)
