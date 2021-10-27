from django.db.models.fields import FloatField
from ssrnai.models.organisms import Organisms
from ssrnai.models.conyza.conyza_gene_information import Conyza_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Conyza_Canadensis_Expression(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Conyza_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    Water_1T_r1 = FloatField(("Water_1T_r1"), null=True, blank=True)
    Water_1T_r2 = FloatField(("Water_1T_r2"), null=True, blank=True)
    Water_1T_r3 = FloatField(("Water_1T_r3"), null=True, blank=True)
    Water_1T_r4 = FloatField(("Water_1T_r4"), null=True, blank=True)
    Water_6T_r1 = FloatField(("Water_6T_r1"), null=True, blank=True)
    Water_6T_r2 = FloatField(("Water_6T_r2"), null=True, blank=True)
    Water_6T_r3 = FloatField(("Water_6T_r3"), null=True, blank=True)
    Water_6T_r4 = FloatField(("Water_6T_r4"), null=True, blank=True)
    D_2_4_1T_r1 = FloatField(("D_2_4_1T_r1"), null=True, blank=True)
    D_2_4_1T_r2 = FloatField(("D_2_4_1T_r2"), null=True, blank=True)
    D_2_4_1T_r3 = FloatField(("D_2_4_1T_r3"), null=True, blank=True)
    D_2_4_1T_r4 = FloatField(("D_2_4_1T_r4"), null=True, blank=True)
    D_2_4_6T_r1 = FloatField(("D_2_4_6T_r1"), null=True, blank=True)
    D_2_4_6T_r2 = FloatField(("D_2_4_6T_r2"), null=True, blank=True)
    D_2_4_6T_r3 = FloatField(("D_2_4_6T_r3"), null=True, blank=True)
    D_2_4_6T_r4 = FloatField(("D_2_4_6T_r4"), null=True, blank=True)
    Dicamba_1T_r1 = FloatField(("Dicamba_1T_r1"), null=True, blank=True)
    Dicamba_1T_r2 = FloatField(("Dicamba_1T_r2"), null=True, blank=True)
    Dicamba_1T_r3 = FloatField(("Dicamba_1T_r3"), null=True, blank=True)
    Dicamba_1T_r4 = FloatField(("Dicamba_1T_r4"), null=True, blank=True)
    Dicamba_6T_r1 = FloatField(("Dicamba_6T_r1"), null=True, blank=True)
    Dicamba_6T_r2 = FloatField(("Dicamba_6T_r2"), null=True, blank=True)
    Dicamba_6T_r3 = FloatField(("Dicamba_6T_r3"), null=True, blank=True)
    Dicamba_6T_r4 = FloatField(("Dicamba_6T_r4"), null=True, blank=True)
    HM_1T_r1 = FloatField(("HM_1T_r1"), null=True, blank=True)
    HM_1T_r2 = FloatField(("HM_1T_r2"), null=True, blank=True)
    HM_1T_r3 = FloatField(("HM_1T_r3"), null=True, blank=True)
    HM_1T_r4 = FloatField(("HM_1T_r4"), null=True, blank=True)
    HM_6T_r1 = FloatField(("HM_6T_r1"), null=True, blank=True)
    HM_6T_r2 = FloatField(("HM_6T_r2"), null=True, blank=True)
    HM_6T_r3 = FloatField(("HM_6T_r3"), null=True, blank=True)
    HM_6T_r4 = FloatField(("HM_6T_r4"), null=True, blank=True)
																	
    class Meta:
        ordering = ['id']
        verbose_name = 'expression'
        verbose_name_plural = 'expressions'

    def __str__(self):
        return '%s' % (self.id)
