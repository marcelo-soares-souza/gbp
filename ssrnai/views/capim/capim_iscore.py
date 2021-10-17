from django.views.generic import DetailView
from ssrnai.models.capim.capim_iscore import Capim_Iscore
from ssrnai.models.capim.capim_gene_information import Capim_Gene_Information
from ssrnai.models.capim.capim_dsrna_information import Capim_Dsrna_Information
from ssrnai.models import Database


class CapimIScore(DetailView):
    template_name = 'capim/capim_iscore.html'
    context_object_name = 'iscore'
    model = Capim_Iscore
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CapimIScore, self).get_context_data(**kwargs)
        context['iscore'] = Capim_Iscore.objects.get(id=int(self.kwargs['pk']))
        iscore = context['iscore']
        context['dsRNA'] = Capim_Dsrna_Information.objects.get(id=int(iscore.dsrna_id))
        context['gene'] = Capim_Gene_Information.objects.get(id=int(iscore.gene_id))
        context['database'] = Database.objects.get(id=int(6))

        return context
