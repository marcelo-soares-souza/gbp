from ssrnai.models.organisms import Organisms
from ssrnai.models.capim.capim_gene_information import Capim_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Capim_Off_Targets(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Capim_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    fragment_seq = models.TextField(("fragment_seq"))
    start = models.IntegerField("start")
    end = models.IntegerField(("end"))
    hits = models.IntegerField("hits")
    hits_description = models.TextField(("hits_description"))


    class Meta:
        ordering = ['id']
        verbose_name = 'offtarget'
        verbose_name_plural = 'offtargets'

    def __str__(self):
        return '%s' % (self.id)
