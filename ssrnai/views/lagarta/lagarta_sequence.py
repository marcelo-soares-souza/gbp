from django.views.generic import DetailView
from ssrnai.models.lagarta.lagarta_dsrna_information import Lagarta_Dsrna_Information
from ssrnai.models.lagarta.lagarta_gene_information import Lagarta_Gene_Information
from ssrnai.models import Database

class LagartaSequence(DetailView):
    template_name = 'lagarta/lagarta_sequence.html'
    context_object_name = 'sequence'
    model = Lagarta_Dsrna_Information
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(LagartaSequence, self).get_context_data(**kwargs)
        context['dsrna'] = Lagarta_Dsrna_Information.objects.get(id=int(self.kwargs['pk']))
        dsrna = context['dsrna']
        context['gene'] = Lagarta_Gene_Information.objects.get(id=int(dsrna.gene_id))
        context['database'] = Database.objects.get(id=int(4))

        return context
