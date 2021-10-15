from django.views.generic import DetailView
from ssrnai.models.nematoide.nematoide_structure import Nematoide_Structure
from ssrnai.models.nematoide.nematoide_gene_information import Nematoide_Gene_Information
from ssrnai.models.nematoide.nematoide_dsrna_information import Nematoide_Dsrna_Information

class NematoideStructure(DetailView):
    template_name = 'nematoide/nematoide_structure.html'
    context_object_name = 'structure'
    model = Nematoide_Structure
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NematoideStructure, self).get_context_data(**kwargs)
        context['structure'] = Nematoide_Structure.objects.get(id=int(self.kwargs['pk']))
        structure = context['structure']
        context['dsRNA'] = Nematoide_Dsrna_Information.objects.get(id=int(structure.dsrna_id))
        context['gene'] = Nematoide_Gene_Information.objects.get(id=int(structure.gene_id))

        return context
