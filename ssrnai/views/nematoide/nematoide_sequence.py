from django.views.generic import DetailView
from ssrnai.models.nematoide.nematoide_dsrna_information import Nematoide_Dsrna_Information
from ssrnai.models.nematoide.nematoide_gene_information import Nematoide_Gene_Information


class NematoideSequence(DetailView):
    template_name = 'nematoide/nematoide_sequence.html'
    context_object_name = 'sequence'
    model = Nematoide_Dsrna_Information
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NematoideSequence, self).get_context_data(**kwargs)
        context['dsrna'] = Nematoide_Dsrna_Information.objects.get(id=int(self.kwargs['pk']))
        dsrna = context['dsrna']
        context['gene'] = Nematoide_Gene_Information.objects.get(id=int(dsrna.gene_id))

        return context
