from django.db.models.fields import FloatField
from ssrnai.models.organisms import Organisms
from ssrnai.models.nematoide.nematoide_gene_information import Nematoide_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Nematoide_Expression(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Nematoide_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    MI_egg_2 = FloatField(("MI_egg_2"), null=True, blank=True)
    MI_J3_3 = FloatField(("MI_J3_3"), null=True, blank=True)
    MI_J4_3 = FloatField(("MI_J4_3"), null=True, blank=True)
    MI_J4_2 = FloatField(("MI_J4_2"), null=True, blank=True)
    MI_egg_1 = FloatField(("MI_egg_1"), null=True, blank=True)
    MI_J4_1 = FloatField(("MI_J4_1"), null=True, blank=True)
    MI_female_2 = FloatField(("MI_female_2"), null=True, blank=True)
    MI_female_1 = FloatField(("MI_female_1"), null=True, blank=True)
    MI_female_3 = FloatField(("MI_female_3"), null=True, blank=True)
    MI_J2_2 = FloatField(("MI_J2_2"), null=True, blank=True)
    MI_J3_1 = FloatField(("MI_J2_3"), null=True, blank=True)
    MI_J2_3 = FloatField(("MI_J2_3"), null=True, blank=True)
    MI_J3_2 = FloatField(("MI_J3_2"), null=True, blank=True)
    MI_J2_1 = FloatField(("MI_J2_1"), null=True, blank=True)
    MI_egg_3 = FloatField(("MI_egg_3"), null=True, blank=True)
    Nig_2_Rep3 = FloatField(("Nig_2_Rep3"), null=True, blank=True)
    Nig_2_Rep2 = FloatField(("Nig_2_Rep2"), null=True, blank=True)
    Ken_1_Rep2 = FloatField(("Ken_1_Rep2"), null=True, blank=True)
    Nig_3_Rep1 = FloatField(("Nig_3_Rep1"), null=True, blank=True)
    Nig_2_Rep1 = FloatField(("Nig_2_Rep1"), null=True, blank=True)
    Nig_1_Rep3 = FloatField(("Nig_1_Rep3"), null=True, blank=True)
    Nig_1_Rep2 = FloatField(("Nig_1_Rep2"), null=True, blank=True)
    Nig_1_Rep1 = FloatField(("Nig_1_Rep1"), null=True, blank=True)
    Ken_1_Rep3 = FloatField(("Ken_1_Rep3"), null=True, blank=True)
    Nig_3_Rep2 = FloatField(("Nig_3_Rep2"), null=True, blank=True)
    Nig_3_Rep3 = FloatField(("Nig_3_Rep3"), null=True, blank=True)
    Ken_1_Rep1 = FloatField(("Ken_1_Rep1"), null=True, blank=True)


																										




    class Meta:
        ordering = ['id']
        verbose_name = 'expression'
        verbose_name_plural = 'expressions'

    def __str__(self):
        return '%s' % (self.id)
