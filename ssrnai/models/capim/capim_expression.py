from django.db.models.fields import FloatField
from ssrnai.models.organisms import Organisms
from ssrnai.models.capim.capim_gene_information import Capim_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Capim_Expression(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Capim_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    exilis_Spike = FloatField(("exilis_Spike"), null=True, blank=True)
    exilis_Grain = FloatField(("exilis_Grain"), null=True, blank=True)
    exilis_Seedling = FloatField(("exilis_Seedling"), null=True, blank=True)
    exilis_leaf = FloatField(("exilis_leaf"), null=True, blank=True)
    exilis_whole = FloatField(("exilis_whole"), null=True, blank=True)
    eriantha_whole = FloatField(("eriantha_whole"), null=True, blank=True)
    cuyabensis_whole = FloatField(("cuyabensis_whole"), null=True, blank=True)
    sanguinalis_Resist1 = FloatField(("sanguinalis_Resist1"), null=True, blank=True)
    sanguinalis_Resist2 = FloatField(("sanguinalis_Resist2"), null=True, blank=True)
    sanguinalis_Suscep1 = FloatField(("sanguinalis_Suscep1"), null=True, blank=True)
    sanguinalis_Suscep2 = FloatField(("sanguinalis_Suscep2"), null=True, blank=True)
    ciliaris_leaves = FloatField(("ciliaris_leaves"), null=True, blank=True)
    ciliaris_roots = FloatField(("ciliaris_roots"), null=True, blank=True)
    ciliaris_leave = FloatField(("ciliaris_leave"), null=True, blank=True)
    ciliaris_root = FloatField(("ciliaris_root"), null=True, blank=True)
    milanjiana_Whole = FloatField(("milanjiana_Whole"), null=True, blank=True)
    californica_leaf1 = FloatField(("californica_leaf1"), null=True, blank=True)
    californica_leaf2 = FloatField(("californica_leaf2"), null=True, blank=True)
    californica_leaf3 = FloatField(("californica_leaf3"), null=True, blank=True)
    californica_leaf4 = FloatField(("californica_leaf4"), null=True, blank=True)
    californica_leaf5 = FloatField(("californica_leaf5"), null=True, blank=True)
    californica_leaf6 = FloatField(("californica_leaf6"), null=True, blank=True)
    ciliaris_Resist1 = FloatField(("ciliaris_Resist1"), null=True, blank=True)
    ciliaris_Resist2 = FloatField(("ciliaris_Resist2"), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'expression'
        verbose_name_plural = 'expressions'

    def __str__(self):
        return '%s' % (self.id)
