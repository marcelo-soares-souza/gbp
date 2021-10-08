from ssrnai.models.organisms import Organisms
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Percevejo_Iscore(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Percevejo_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    fragment_seq = models.TextField(("fragment_seq"), max_length=100)
    start = models.IntegerField(("start"))
    end = models.IntegerField(("end"))
    hits= models.IntegerField("hits")
    hits_description = models.TextField(("hits_description"))


    class Meta:
        ordering = ['id']
        verbose_name = 'dsrna'
        verbose_name_plural = 'dsrnas'

    def __str__(self):
        return '%s' % (self.dsrna_name)
