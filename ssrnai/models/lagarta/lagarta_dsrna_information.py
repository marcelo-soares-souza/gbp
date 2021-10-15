from ssrnai.models.organisms import Organisms
from ssrnai.models.lagarta.lagarta_gene_information import Lagarta_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Lagarta_Dsrna_Information(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Lagarta_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    dsrna_name = models.CharField(("dsrna_name"), max_length=100)
    start = models.IntegerField(("start"), null=True, blank=True)
    stop = models.IntegerField(("stop"), null=True, blank=True)
    length = models.IntegerField(("length"), null=True, blank=True)
    dsrna_seq = models.CharField(("dsrna_seq"), max_length=2000, null=True, blank=True)
    offtarget_image = models.TextField(("offtarget_image"), null=True, blank=True)


    class Meta:
        ordering = ['id']
        verbose_name = 'dsrna'
        verbose_name_plural = 'dsrnas'

    def __str__(self):
        return '%s' % (self.dsrna_name)
