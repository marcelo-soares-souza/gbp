from django.db.models.fields import FloatField
from ssrnai.models.organisms import Organisms
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information
from ssrnai.models.percevejo.percevejo_dsrna_information import PercevejoDsrnaInformation
from django.db import models
from projeto.models.template import TemplateModelMixin

class Percevejo_Expression(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Percevejo_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    eheros_fat_body1 = FloatField(("eheros_fat_body1"), null=True, blank=True)
    eheros_fat_body2 = FloatField(("eheros_fat_body2"), null=True, blank=True)
    eheros_fat_body3 = FloatField(("eheros_fat_body3"), null=True, blank=True)
    eheros_fat_body4 = FloatField(("eheros_fat_body4"), null=True, blank=True)
    eheros_gut1 = FloatField(("eheros_gut1"), null=True, blank=True)
    eheros_fat_body5 = FloatField(("eheros_fat_body5"), null=True, blank=True)
    eheros_gut2 = FloatField(("eheros_gut2"), null=True, blank=True)
    eheros_gut3 = FloatField(("eheros_gut3"), null=True, blank=True)
    eheros_gut4 = FloatField(("eheros_gut4"), null=True, blank=True)
    eheros_gut5 = FloatField(("eheros_gut5"), null=True, blank=True)
    eheros_gut6 = FloatField(("eheros_gut6"), null=True, blank=True)
    eheros_gut7 = FloatField(("eheros_gut7"), null=True, blank=True)
    eheros_gut8 = FloatField(("eheros_gut8"), null=True, blank=True)
    eheros_gut9 = FloatField(("eheros_gut9"), null=True, blank=True)
    eheros_gut10 = FloatField(("eheros_gut10"), null=True, blank=True)
    eheros_gut11 = FloatField(("eheros_gut11"), null=True, blank=True)
    eheros_gut12 = FloatField(("eheros_gut12"), null=True, blank=True)
    eheros_gut13 = FloatField(("eheros_gut13"), null=True, blank=True)



    class Meta:
        ordering = ['id']
        verbose_name = 'dicer'
        verbose_name_plural = 'dicers'

    def __str__(self):
        return '%s' % (self.id)
