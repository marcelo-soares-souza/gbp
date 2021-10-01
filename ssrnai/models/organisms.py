from ssrnai.models.database import Database
from django.db import models
from projeto.models.template import TemplateModelMixin

class Organisms(models.Model, TemplateModelMixin):

    database = models.ForeignKey(Database("database_id"), null=True, blank=True, on_delete=models.SET_NULL)
    organism_name = models.CharField(("organism_name"), max_length=150, unique=True)
    common_name = models.CharField(("common_name"), max_length=150)
    taxonomy = models.CharField(("taxonomy"), max_length=1000, null=True, blank=True)

    class Meta:
        ordering = ['organism_name']
        verbose_name = 'organism'
        verbose_name_plural = 'organisms'

    def __str__(self):
        return '%s' % (self.organism_name)
