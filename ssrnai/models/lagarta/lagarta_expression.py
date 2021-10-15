from django.db.models.fields import FloatField
from ssrnai.models.organisms import Organisms
from ssrnai.models.lagarta.lagarta_gene_information import Lagarta_Gene_Information
from django.db import models
from projeto.models.template import TemplateModelMixin

class Lagarta_Expression(models.Model, TemplateModelMixin):

    organism = models.ForeignKey(Organisms("organism_id"), null=True, blank=True, on_delete=models.SET_NULL)
    gene = models.ForeignKey(Lagarta_Gene_Information("gene_id"), null=True, blank=True, on_delete=models.SET_NULL)
    larvae1 = FloatField(("larvae1"), null=True, blank=True)
    larvae2 = FloatField(("larvae2"), null=True, blank=True)
    larvae3 = FloatField(("larvae3"), null=True, blank=True)
    larvae4 = FloatField(("larvae4"), null=True, blank=True)
    larvae5 = FloatField(("larvae5"), null=True, blank=True)
    larvae6 = FloatField(("larvae6"), null=True, blank=True)
    larvae7 = FloatField(("larvae7"), null=True, blank=True)
    larvae8 = FloatField(("larvae8"), null=True, blank=True)
    larvae9 = FloatField(("larvae9"), null=True, blank=True)
    larvae10 = FloatField(("larvae10"), null=True, blank=True)
    larvae11 = FloatField(("larvae11"), null=True, blank=True)
    larvae12 = FloatField(("larvae12"), null=True, blank=True)
    larvae13 = FloatField(("larvae13"), null=True, blank=True)
    larvae14 = FloatField(("larvae14"), null=True, blank=True)
    larvae15 = FloatField(("larvae15"), null=True, blank=True)
    larvae16 = FloatField(("larvae16"), null=True, blank=True)
    larvae17 = FloatField(("larvae17"), null=True, blank=True)
    larvae18 = FloatField(("larvae18"), null=True, blank=True)
    larvae19 = FloatField(("larvae19"), null=True, blank=True)
    larvae20 = FloatField(("larvae20"), null=True, blank=True)
    larvae21 = FloatField(("larvae21"), null=True, blank=True)
    larvae22 = FloatField(("larvae22"), null=True, blank=True)
    larvae23 = FloatField(("larvae23"), null=True, blank=True)
    larvae24 = FloatField(("larvae24"), null=True, blank=True)
    larvae25 = FloatField(("larvae25"), null=True, blank=True)
    larvae26 = FloatField(("larvae26"), null=True, blank=True)
    larvae27 = FloatField(("larvae27"), null=True, blank=True)
    larvae28 = FloatField(("larvae28"), null=True, blank=True)
    larvae29 = FloatField(("larvae29"), null=True, blank=True)
    larvae30 = FloatField(("larvae30"), null=True, blank=True)
    larvae31 = FloatField(("larvae31"), null=True, blank=True)
    larvae32 = FloatField(("larvae32"), null=True, blank=True)
    larvae33 = FloatField(("larvae33"), null=True, blank=True)
    larvae34 = FloatField(("larvae34"), null=True, blank=True)
    larvae35 = FloatField(("larvae35"), null=True, blank=True)
    larvae36 = FloatField(("larvae36"), null=True, blank=True)
    larvae37 = FloatField(("larvae37"), null=True, blank=True)
    larvae38 = FloatField(("larvae38"), null=True, blank=True)
    larvae39 = FloatField(("larvae39"), null=True, blank=True)
    larvae40 = FloatField(("larvae40"), null=True, blank=True)
    larvae41 = FloatField(("larvae41"), null=True, blank=True)
    larvae42 = FloatField(("larvae42"), null=True, blank=True)
    larvae43 = FloatField(("larvae43"), null=True, blank=True)
    larvae44 = FloatField(("larvae44"), null=True, blank=True)
    larvae45 = FloatField(("larvae45"), null=True, blank=True)
    larvae46 = FloatField(("larvae46"), null=True, blank=True)
    larvae47 = FloatField(("larvae47"), null=True, blank=True)
    larvae48 = FloatField(("larvae48"), null=True, blank=True)
    larvae49 = FloatField(("larvae49"), null=True, blank=True)
    larvae50 = FloatField(("larvae50"), null=True, blank=True)
    larvae51 = FloatField(("larvae51"), null=True, blank=True)
    larvae52 = FloatField(("larvae52"), null=True, blank=True)
    larvae53 = FloatField(("larvae53"), null=True, blank=True)
    larvae54 = FloatField(("larvae54"), null=True, blank=True)
    larvae55 = FloatField(("larvae55"), null=True, blank=True)
    larvae56 = FloatField(("larvae56"), null=True, blank=True)
    larvae57 = FloatField(("larvae57"), null=True, blank=True)
    larvae58 = FloatField(("larvae58"), null=True, blank=True)
    larvae59 = FloatField(("larvae59"), null=True, blank=True)
    larvae60 = FloatField(("larvae60"), null=True, blank=True)
    larvae61 = FloatField(("larvae61"), null=True, blank=True)
    larvae62 = FloatField(("larvae62"), null=True, blank=True)
    larvae63 = FloatField(("larvae63"), null=True, blank=True)
    larvae64 = FloatField(("larvae64"), null=True, blank=True)
    larvae65 = FloatField(("larvae65"), null=True, blank=True)
    larvae66 = FloatField(("larvae66"), null=True, blank=True)
    larvae67 = FloatField(("larvae67"), null=True, blank=True)
    larvae68 = FloatField(("larvae68"), null=True, blank=True)
    larvae69 = FloatField(("larvae69"), null=True, blank=True)
    larvae70 = FloatField(("larvae70"), null=True, blank=True)
    larvae71 = FloatField(("larvae71"), null=True, blank=True)
    larvae72 = FloatField(("larvae72"), null=True, blank=True)
    larvae73 = FloatField(("larvae73"), null=True, blank=True)
    larvae74 = FloatField(("larvae74"), null=True, blank=True)
    larvae75 = FloatField(("larvae75"), null=True, blank=True)
    larvae76 = FloatField(("larvae76"), null=True, blank=True)
    larvae77 = FloatField(("larvae77"), null=True, blank=True)
    larvae78 = FloatField(("larvae78"), null=True, blank=True)
    larvae79 = FloatField(("larvae79"), null=True, blank=True) 
    larvae80 = FloatField(("larvae80"), null=True, blank=True)
    larvae81 = FloatField(("larvae81"), null=True, blank=True)
    larvae82 = FloatField(("larvae82"), null=True, blank=True)
    larvae83 = FloatField(("larvae83"), null=True, blank=True)
    larvae84 = FloatField(("larvae84"), null=True, blank=True)
    larvae85 = FloatField(("larvae85"), null=True, blank=True)
    larvae86 = FloatField(("larvae86"), null=True, blank=True)
    larvae87 = FloatField(("larvae87"), null=True, blank=True)
    larvae88 = FloatField(("larvae88"), null=True, blank=True)
    larvae89 = FloatField(("larvae89"), null=True, blank=True)
    larvae90 = FloatField(("larvae90"), null=True, blank=True)
    larvae91 = FloatField(("larvae91"), null=True, blank=True)
    larvae92 = FloatField(("larvae92"), null=True, blank=True)
    larvae93 = FloatField(("larvae93"), null=True, blank=True)
    larvae94 = FloatField(("larvae94"), null=True, blank=True)
    larvae95 = FloatField(("larvae95"), null=True, blank=True)
    larvae96 = FloatField(("larvae96"), null=True, blank=True)
    larvae97 = FloatField(("larvae97"), null=True, blank=True)
    larvae98 = FloatField(("larvae98"), null=True, blank=True)
    larvae99 = FloatField(("larvae99"), null=True, blank=True)
    larvae100 = FloatField(("larvae100"), null=True, blank=True)
    larvae101 = FloatField(("larvae101"), null=True, blank=True)
    larvae102 = FloatField(("larvae102"), null=True, blank=True)
    larvae103 = FloatField(("larvae103"), null=True, blank=True)
    larvae104 = FloatField(("larvae104"), null=True, blank=True)
    larvae105 = FloatField(("larvae105"), null=True, blank=True)
    larvae106 = FloatField(("larvae106"), null=True, blank=True)
    larvae107 = FloatField(("larvae107"), null=True, blank=True)
    larvae108 = FloatField(("larvae108"), null=True, blank=True)
    larvae109 = FloatField(("larvae109"), null=True, blank=True)
    larvae110 = FloatField(("larvae110"), null=True, blank=True)
    larvae111 = FloatField(("larvae111"), null=True, blank=True)
    larvae112 = FloatField(("larvae112"), null=True, blank=True)
    larvae113 = FloatField(("larvae113"), null=True, blank=True)
    larvae114 = FloatField(("larvae114"), null=True, blank=True)
    larvae115 = FloatField(("larvae115"), null=True, blank=True)
    larvae116 = FloatField(("larvae116"), null=True, blank=True)
    larvae117 = FloatField(("larvae117"), null=True, blank=True)
    larvae118 = FloatField(("larvae118"), null=True, blank=True)
    larvae119 = FloatField(("larvae119"), null=True, blank=True)
    larvae120 = FloatField(("larvae120"), null=True, blank=True)
    larvae121 = FloatField(("larvae121"), null=True, blank=True)
    larvae122 = FloatField(("larvae122"), null=True, blank=True)
    larvae123 = FloatField(("larvae123"), null=True, blank=True)
    larvae124 = FloatField(("larvae124"), null=True, blank=True)
    larvae125 = FloatField(("larvae125"), null=True, blank=True)
    larvae126 = FloatField(("larvae126"), null=True, blank=True)
    larvae127 = FloatField(("larvae127"), null=True, blank=True)
    larvae128 = FloatField(("larvae128"), null=True, blank=True)
    fatboy1 = FloatField(("fatboy1"), null=True, blank=True)
    fatboy2 = FloatField(("fatboy2"), null=True, blank=True)
    fatboy3 = FloatField(("fatboy3"), null=True, blank=True)
    fatboy4 = FloatField(("fatboy4"), null=True, blank=True)
    fatboy5 = FloatField(("fatboy5"), null=True, blank=True)
    fatboy6 = FloatField(("fatboy6"), null=True, blank=True)
    hemocytes1 = FloatField(("hemocytes1"), null=True, blank=True)
    hemocytes2 = FloatField(("hemocytes2"), null=True, blank=True)
    hemocytes3 = FloatField(("hemocytes3"), null=True, blank=True)
    hemocytes4 = FloatField(("hemocytes4"), null=True, blank=True)
    midgut1 = FloatField(("midgut1"), null=True, blank=True)
    midgut2 = FloatField(("midgut2"), null=True, blank=True)
    midgut3 = FloatField(("midgut3"), null=True, blank=True)
    midgut4 = FloatField(("midgut4"), null=True, blank=True)
    midgut5 = FloatField(("midgut5"), null=True, blank=True)
    midgut6 = FloatField(("midgut6"), null=True, blank=True)
    fatboy7 = FloatField(("fatboy7"), null=True, blank=True)
    fatboy8 = FloatField(("fatboy8"), null=True, blank=True)
    fatboy9 = FloatField(("fatboy9"), null=True, blank=True)
    fatboy10 = FloatField(("fatboy10"), null=True, blank=True)
    fatboy11 = FloatField(("fatboy11"), null=True, blank=True)
    fatboy12 = FloatField(("fatboy12"), null=True, blank=True)
    hemocytes5 = FloatField(("hemocytes5"), null=True, blank=True)
    hemocytes6 = FloatField(("hemocytes6"), null=True, blank=True)
    hemocytes7 = FloatField(("hemocytes7"), null=True, blank=True)
    midgut7 = FloatField(("midgut7"), null=True, blank=True)
    midgut8 = FloatField(("midgut8"), null=True, blank=True)
    midgut9 = FloatField(("midgut9"), null=True, blank=True)
    midgut10 = FloatField(("midgut10"), null=True, blank=True)
    midgut11 = FloatField(("midgut11"), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'expression'
        verbose_name_plural = 'expressions'

    def __str__(self):
        return '%s' % (self.id)