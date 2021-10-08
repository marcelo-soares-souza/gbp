from ssrnai.models.organisms import Organisms
from ssrnai.models.conyza.conyza_gene_information import Conyza_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Conyza_Dsrna_Information(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Conyza_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    dsrna_name = models.CharField(("dsrna_name"), max_length=100)
    start = models.IntegerField(("start"))
    stop = models.IntegerField(("stop"))
    length = models.IntegerField("length")
    dsrna_seq = models.TextField(("dsrna_seq"))


    class Meta:
        ordering = ['id']
        verbose_name = 'dsrna'
        verbose_name_plural = 'dsrnas'

    def __str__(self):
        return '%s' % (self.dsrna_name)
