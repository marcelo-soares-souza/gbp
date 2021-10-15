from django.views.generic import DetailView
from ssrnai.models.lagarta.lagarta_dicer import Lagarta_Dicer
from ssrnai.models.lagarta.lagarta_gene_information import Lagarta_Gene_Information
from ssrnai.models.lagarta.lagarta_dsrna_information import Lagarta_Dsrna_Information

class LagartaDicer(DetailView):
    template_name = 'lagarta/lagarta_dicer.html'
    context_object_name = 'dicer'
    model = Lagarta_Dicer
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(LagartaDicer, self).get_context_data(**kwargs)
        context['dicer'] = Lagarta_Dicer.objects.get(id=int(self.kwargs['pk']))
        dicer = context['dicer']
        context['dsRNA'] = Lagarta_Dsrna_Information.objects.get(id=int(dicer.dsrna_id))
        context['gene'] = Lagarta_Gene_Information.objects.get(id=int(dicer.gene_id))

        return context
