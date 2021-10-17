from django.views.generic import DetailView
from ssrnai.models import Database
from ssrnai.models.percevejo.percevejo_iscore import Percevejo_Iscore
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information
from ssrnai.models.percevejo.percevejo_dsrna_information import PercevejoDsrnaInformation


class PercevejoIScore(DetailView):
    template_name = 'percevejo/percevejo_iscore.html'
    context_object_name = 'iscore'
    model = Percevejo_Iscore
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PercevejoIScore, self).get_context_data(**kwargs)
        context['iscore'] = Percevejo_Iscore.objects.get(id=int(self.kwargs['pk']))
        iscore = context['iscore']
        context['dsRNA'] = PercevejoDsrnaInformation.objects.get(id=int(iscore.dsrna_id))
        context['gene'] = Percevejo_Gene_Information.objects.get(id=int(iscore.gene_id))
        context['database'] = Database.objects.get(id=int(5))

        return context
