from django.views.generic import DetailView
from ssrnai.models.conyza.conyza_structure import Conyza_Structure
from ssrnai.models.conyza.conyza_gene_information import Conyza_Gene_Information
from ssrnai.models.conyza.conyza_dsrna_information import Conyza_Dsrna_Information


class BuvaStructure(DetailView):
    template_name = 'buva/buva_structure.html'
    context_object_name = 'structure'
    model = Conyza_Structure
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(BuvaStructure, self).get_context_data(**kwargs)
        context['structure'] = Conyza_Structure.objects.get(id=int(self.kwargs['pk']))
        structure = context['structure']
        context['dsRNA'] = Conyza_Dsrna_Information.objects.get(id=int(structure.dsrna_id))
        context['gene'] = Conyza_Gene_Information.objects.get(id=int(structure.gene_id))

        return context
