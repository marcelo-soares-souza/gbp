from django.views.generic import DetailView
from ssrnai.models.conyza.conyza_dsrna_information import Conyza_Dsrna_Information
from ssrnai.models.conyza.conyza_gene_information import Conyza_Gene_Information
from ssrnai.models import Database

class BuvaSequence(DetailView):
    template_name = 'buva/buva_sequence.html'
    context_object_name = 'sequence'
    model = Conyza_Dsrna_Information
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(BuvaSequence, self).get_context_data(**kwargs)
        context['dsrna'] = Conyza_Dsrna_Information.objects.get(id=int(self.kwargs['pk']))
        dsrna = context['dsrna']
        context['gene'] = Conyza_Gene_Information.objects.get(id=int(dsrna.gene_id))
        context['database'] = Database.objects.get(id=int(1))

        return context
