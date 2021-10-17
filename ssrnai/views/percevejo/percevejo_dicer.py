from django.views.generic import DetailView
from ssrnai.models import Database
from ssrnai.models.percevejo.percevejo_dicer import Percevejo_Dicer
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information
from ssrnai.models.percevejo.percevejo_dsrna_information import PercevejoDsrnaInformation


class PercevejoDicer(DetailView):
    template_name = 'percevejo/percevejo_dicer.html'
    context_object_name = 'dicer'
    model = Percevejo_Dicer
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PercevejoDicer, self).get_context_data(**kwargs)
        context['dicer'] = Percevejo_Dicer.objects.get(id=int(self.kwargs['pk']))
        dicer = context['dicer']
        context['dsRNA'] = PercevejoDsrnaInformation.objects.get(id=int(dicer.dsrna_id))
        context['gene'] = Percevejo_Gene_Information.objects.get(id=int(dicer.gene_id))
        context['database'] = Database.objects.get(id=int(5))

        return context
