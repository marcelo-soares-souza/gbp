from django.views.generic import DetailView
from ssrnai.models.percevejo.percevejo_structure import Percevejo_Structure
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information
from ssrnai.models.percevejo.percevejo_dsrna_information import PercevejoDsrnaInformation
from ssrnai.models import Database

class PercevejoStructure(DetailView):
    template_name = 'percevejo/percevejo_structure.html'
    context_object_name = 'structure'
    model = Percevejo_Structure
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PercevejoStructure, self).get_context_data(**kwargs)
        context['structure'] = Percevejo_Structure.objects.get(id=int(self.kwargs['pk']))
        structure = context['structure']
        context['dsRNA'] = PercevejoDsrnaInformation.objects.get(id=int(structure.dsrna_id))
        context['gene'] = Percevejo_Gene_Information.objects.get(id=int(structure.gene_id))
        context['database'] = Database.objects.get(id=int(5))

        return context
