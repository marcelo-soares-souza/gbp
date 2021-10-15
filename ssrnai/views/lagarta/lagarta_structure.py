from django.views.generic import DetailView
from ssrnai.models.lagarta.lagarta_structure import Lagarta_Structure
from ssrnai.models.lagarta.lagarta_gene_information import Lagarta_Gene_Information
from ssrnai.models.lagarta.lagarta_dsrna_information import Lagarta_Dsrna_Information

class LagartaStructure(DetailView):
    template_name = 'lagarta/lagarta_structure.html'
    context_object_name = 'structure'
    model = Lagarta_Structure
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(LagartaStructure, self).get_context_data(**kwargs)
        context['structure'] = Lagarta_Structure.objects.get(id=int(self.kwargs['pk']))
        structure = context['structure']
        context['dsRNA'] = Lagarta_Dsrna_Information.objects.get(id=int(structure.dsrna_id))
        context['gene'] = Lagarta_Gene_Information.objects.get(id=int(structure.gene_id))

        return context
