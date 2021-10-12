from django.views.generic import DetailView
from ssrnai.models.percevejo.percevejo_dsrna_information import PercevejoDsrnaInformation
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information


class PercevejoSequence(DetailView):
    template_name = 'percevejo/percevejo_sequence.html'
    context_object_name = 'sequence'
    model = PercevejoDsrnaInformation
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PercevejoSequence, self).get_context_data(**kwargs)
        context['dsrna'] = PercevejoDsrnaInformation.objects.get(id=int(self.kwargs['pk']))
        dsrna = context['dsrna']
        context['gene'] = Percevejo_Gene_Information.objects.get(id=int(dsrna.gene_id))

        return context
