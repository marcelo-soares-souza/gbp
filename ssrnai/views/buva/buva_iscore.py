from django.views.generic import DetailView
from ssrnai.models.conyza.conyza_iscore import Conyza_Iscore
from ssrnai.models.conyza.conyza_gene_information import Conyza_Gene_Information
from ssrnai.models.conyza.conyza_dsrna_information import Conyza_Dsrna_Information
from ssrnai.models import Database


class BuvaIScore(DetailView):
    template_name = 'buva/buva_iscore.html'
    context_object_name = 'iscore'
    model = Conyza_Iscore
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(BuvaIScore, self).get_context_data(**kwargs)
        context['iscore'] = Conyza_Iscore.objects.get(id=int(self.kwargs['pk']))
        iscore = context['iscore']
        context['dsRNA'] = Conyza_Dsrna_Information.objects.get(id=int(iscore.dsrna_id))
        context['gene'] = Conyza_Gene_Information.objects.get(id=int(iscore.gene_id))
        context['database'] = Database.objects.get(id=int(1))

        return context
