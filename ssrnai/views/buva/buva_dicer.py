from django.views.generic import DetailView
from ssrnai.models.conyza.conyza_dicer import Conyza_Dicer
from ssrnai.models.conyza.conyza_gene_information import Conyza_Gene_Information
from ssrnai.models.conyza.conyza_dsrna_information import Conyza_Dsrna_Information


class BuvaDicer(DetailView):
    template_name = 'buva/buva_dicer.html'
    context_object_name = 'dicer'
    model = Conyza_Dicer
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(BuvaDicer, self).get_context_data(**kwargs)
        context['dicer'] = Conyza_Dicer.objects.get(id=int(self.kwargs['pk']))
        dicer = context['dicer']
        context['dsRNA'] = Conyza_Dsrna_Information.objects.get(id=int(dicer.dsrna_id))
        context['gene'] = Conyza_Gene_Information.objects.get(id=int(dicer.gene_id))

        return context
