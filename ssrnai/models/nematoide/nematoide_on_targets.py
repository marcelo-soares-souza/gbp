from ssrnai.models.organisms import Organisms
from ssrnai.models.nematoide.nematoide_gene_information import Nematoide_Gene_Information
from ssrnai.models.nematoide.nematoide_dsrna_information import Nematoide_Dsrna_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Nematoide_On_Targets(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Nematoide_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    dsrna = models.ForeignKey(Nematoide_Dsrna_Information("dsrna_id"), null=True, blank=True, on_delete=models.SET_NULL)
    number_ontarget = models.IntegerField(("number_ontarget"), null=True, blank=True)
    start_dsrna = models.IntegerField(("start_dsrna"), null=True, blank=True)
    end_dsrna = models.IntegerField(("end_dsrna"), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'ontarget'
        verbose_name_plural = 'ontargets'

    def __str__(self):
        return '%s' % (self.id)
