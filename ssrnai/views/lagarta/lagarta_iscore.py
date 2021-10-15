from django.views.generic import DetailView
from ssrnai.models.lagarta.lagarta_iscore import Lagarta_Iscore
from ssrnai.models.lagarta.lagarta_gene_information import Lagarta_Gene_Information
from ssrnai.models.lagarta.lagarta_dsrna_information import Lagarta_Dsrna_Information

class LagartaIScore(DetailView):
    template_name = 'lagarta/lagarta_iscore.html'
    context_object_name = 'iscore'
    model = Lagarta_Iscore
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(LagartaIScore, self).get_context_data(**kwargs)
        context['iscore'] = Lagarta_Iscore.objects.get(id=int(self.kwargs['pk']))
        iscore = context['iscore']
        context['dsRNA'] = Lagarta_Dsrna_Information.objects.get(id=int(iscore.dsrna_id))
        context['gene'] = Lagarta_Gene_Information.objects.get(id=int(iscore.gene_id))

        return context
