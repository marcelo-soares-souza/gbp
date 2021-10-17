from django.views.generic import DetailView
from ssrnai.models.capim.capim_structure import Capim_Structure
from ssrnai.models.capim.capim_gene_information import Capim_Gene_Information
from ssrnai.models.capim.capim_dsrna_information import Capim_Dsrna_Information
from ssrnai.models import Database

class CapimStructure(DetailView):
    template_name = 'capim/capim_structure.html'
    context_object_name = 'structure'
    model = Capim_Structure
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CapimStructure, self).get_context_data(**kwargs)
        context['structure'] = Capim_Structure.objects.get(id=int(self.kwargs['pk']))
        structure = context['structure']
        context['dsRNA'] = Capim_Dsrna_Information.objects.get(id=int(structure.dsrna_id))
        context['gene'] = Capim_Gene_Information.objects.get(id=int(structure.gene_id))
        context['database'] = Database.objects.get(id=int(6))

        return context
