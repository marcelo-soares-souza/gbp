from ssrnai.models.organisms import Organisms
from django.db import models
from projeto.models.template import TemplateModelMixin

class Conyza_Gene_Information(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene_name = models.CharField(("gene_name"), max_length=250)
    length = models.IntegerField(("length"), null=True, blank=True)
    cds_seq = models.TextField(("cds_seq"), null=True, blank=True)
    gene_description = models.TextField(("gene_description"), null=True, blank=True)
    sprot_top_blastx_hit = models.TextField(("sprot_top_blastx_hit"), null=True, blank=True)
    pfam = models.TextField(("pfam"), null=True, blank=True)
    kegg = models.TextField(("kegg"), null=True, blank=True)
    gene_ontology_blastx = models.TextField(("gene_ontology_blastx"), null=True, blank=True)
    gene_ontology_pfam = models.TextField(("kegene_ontology_pfamgg"), null=True, blank=True)


    class Meta:
        ordering = ['id']
        verbose_name = 'gene'
        verbose_name_plural = 'genes'

    def __str__(self):
        return '%s' % (self.id)
