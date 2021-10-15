from django.db.models.fields import FloatField
from ssrnai.models.organisms import Organisms
from ssrnai.models.conyza.conyza_gene_information import Conyza_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Conyza_Expression(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Conyza_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    Q17_R1_POST = FloatField(("Q17_R1_POST"), null=True, blank=True)
    Q17_R1_PRE = FloatField(("Q17_R1_PRE"), null=True, blank=True)
    Q17_R5_POST = FloatField(("Q17_R5_POST"), null=True, blank=True)
    Q17_R5_PRE = FloatField(("Q17_R5_PRE"), null=True, blank=True)
    Q21_S4_POST = FloatField(("Q21_S4_POST"), null=True, blank=True)
    Q21_S4_PRE = FloatField(("Q21_S4_PRE"), null=True, blank=True)
    Q21_S5_POST = FloatField(("Q21_S5_POST"), null=True, blank=True)
    Q21_S5_PRE = FloatField(("Q21_S5_PRE"), null=True, blank=True)
    Q21_S7_POST = FloatField(("Q21_S7_POST"), null=True, blank=True)
    Q21_S7_PRE = FloatField(("Q21_S7_PRE"), null=True, blank=True)
    Q34_S1_POST = FloatField(("Q34_S1_POST"), null=True, blank=True)
    Q34_S1_PRE = FloatField(("Q34_S1_PRE"), null=True, blank=True)
    Q34_S2_POST = FloatField(("Q34_S2_POST"), null=True, blank=True)
    Q34_S2_PRE = FloatField(("Q34_S2_PRE"), null=True, blank=True)
    Q34_S5_POST = FloatField(("Q34_S5_POST"), null=True, blank=True)
    Q34_S5_PRE = FloatField(("Q34_S5_PRE"), null=True, blank=True)
    Q42_R4_POST = FloatField(("Q42_R4_POST"), null=True, blank=True)
    Q42_R4_PRE = FloatField(("Q42_R4_PRE"), null=True, blank=True)
    Q42_R5_POST = FloatField(("Q42_R5_POST"), null=True, blank=True)
    Q42_R5_PRE = FloatField(("Q42_R5_PRE"), null=True, blank=True)
    Q42_R6_POST = FloatField(("Q42_R6_POST"), null=True, blank=True)
    Q42_R6_PRE = FloatField(("Q42_R6_PRE"), null=True, blank=True)
																	
    class Meta:
        ordering = ['id']
        verbose_name = 'expression'
        verbose_name_plural = 'expressions'

    def __str__(self):
        return '%s' % (self.id)
