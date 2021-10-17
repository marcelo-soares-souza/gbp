from django.views.generic import DetailView
from ssrnai.models.capim.capim_dsrna_information import Capim_Dsrna_Information
from ssrnai.models.capim.capim_gene_information import Capim_Gene_Information
from ssrnai.models import Database

class CapimSequence(DetailView):
    template_name = 'capim/capim_sequence.html'
    context_object_name = 'sequence'
    model = Capim_Dsrna_Information
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CapimSequence, self).get_context_data(**kwargs)
        context['dsrna'] = Capim_Dsrna_Information.objects.get(id=int(self.kwargs['pk']))
        dsrna = context['dsrna']
        context['gene'] = Capim_Gene_Information.objects.get(id=int(dsrna.gene_id))
        context['database'] = Database.objects.get(id=int(6))

        return context
