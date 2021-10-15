from ssrnai.models.organisms import Organisms
from ssrnai.models.lagarta.lagarta_dsrna_information import Lagarta_Dsrna_Information
from ssrnai.models.lagarta.lagarta_gene_information import Lagarta_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Lagarta_Iscore(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Lagarta_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    dsrna = models.ForeignKey(Lagarta_Dsrna_Information("dsrna_id"), null=True, blank=True, on_delete=models.SET_NULL)
    rank_dsir = models.IntegerField(("rank_dsir"), null=True, blank=True)
    rank_iscore = models.IntegerField(("rank_iscore"), null=True, blank=True)
    rank_sbiopredsi = models.IntegerField(("rank_sbiopredsi"), null=True, blank=True)
    mean_dsir = models.FloatField(("mean_dsir"), null=True, blank=True)
    sum_dsir = models.FloatField(("sum_dsir"), null=True, blank=True)
    max_dsir = models.FloatField(("max_dsir"), null=True, blank=True)
    min_dsir = models.FloatField(("min_dsir"), null=True, blank=True)
    count_dsir = models.FloatField(("count_dsir"), null=True, blank=True)
    median_dsir = models.FloatField(("median_dsir"), null=True, blank=True)
    std_dsir = models.FloatField(("std_dsir"), null=True, blank=True)
    var_dsir = models.FloatField(("var_dsir"), null=True, blank=True)
    mean_iscore = models.FloatField(("mean_iscore"), null=True, blank=True)
    sum_iscore = models.FloatField(("sum_iscore"), null=True, blank=True)
    max_iscore = models.FloatField(("max_iscore"), null=True, blank=True)
    min_iscore = models.FloatField(("min_iscore"), null=True, blank=True)
    count_iscore = models.FloatField(("count_iscore"), null=True, blank=True)
    median_iscore = models.FloatField(("median_iscore"), null=True, blank=True)
    std_iscore = models.FloatField(("std_iscore"), null=True, blank=True)
    var_iscore = models.FloatField(("var_iscore"), null=True, blank=True)
    mean_sbiopredsi = models.FloatField(("mean_iscore"), null=True, blank=True)
    sum_sbiopredsi = models.FloatField(("sum_iscore"), null=True, blank=True)
    max_sbiopredsi = models.FloatField(("max_iscore"), null=True, blank=True)
    min_sbiopredsi = models.FloatField(("min_iscore"), null=True, blank=True)
    count_sbiopredsi = models.FloatField(("count_iscore"), null=True, blank=True)
    median_sbiopredsi = models.FloatField(("median_iscore"), null=True, blank=True)
    std_sbiopredsi = models.FloatField(("std_iscore"), null=True, blank=True)
    var_sbiopredsi = models.FloatField(("var_iscore"), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'iscore'
        verbose_name_plural = 'iscores'

    def __str__(self):
        return '%s' % (self.id)
