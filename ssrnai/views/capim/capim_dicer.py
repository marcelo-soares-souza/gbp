from django.views.generic import DetailView
from ssrnai.models.capim.capim_dicer import Capim_Dicer
from ssrnai.models.capim.capim_gene_information import Capim_Gene_Information
from ssrnai.models.capim.capim_dsrna_information import Capim_Dsrna_Information
from ssrnai.models import Database


class CapimDicer(DetailView):
    template_name = 'capim/capim_dicer.html'
    context_object_name = 'dicer'
    model = Capim_Dicer
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CapimDicer, self).get_context_data(**kwargs)
        context['dicer'] = Capim_Dicer.objects.get(id=int(self.kwargs['pk']))
        dicer = context['dicer']
        context['dsRNA'] = Capim_Dsrna_Information.objects.get(id=int(dicer.dsrna_id))
        context['gene'] = Capim_Gene_Information.objects.get(id=int(dicer.gene_id))
        context['database'] = Database.objects.get(id=int(6))

        return context
