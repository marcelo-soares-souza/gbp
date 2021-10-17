from django.views.generic import DetailView
from ssrnai.models.nematoide.nematoide_dicer import Nematoide_Dicer
from ssrnai.models.nematoide.nematoide_gene_information import Nematoide_Gene_Information
from ssrnai.models.nematoide.nematoide_dsrna_information import Nematoide_Dsrna_Information
from ssrnai.models import Database


class NematoideDicer(DetailView):
    template_name = 'nematoide/nematoide_dicer.html'
    context_object_name = 'dicer'
    model = Nematoide_Dicer
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NematoideDicer, self).get_context_data(**kwargs)
        context['dicer'] = Nematoide_Dicer.objects.get(id=int(self.kwargs['pk']))
        dicer = context['dicer']
        context['dsRNA'] = Nematoide_Dsrna_Information.objects.get(id=int(dicer.dsrna_id))
        context['gene'] = Nematoide_Gene_Information.objects.get(id=int(dicer.gene_id))
        context['database'] = Database.objects.get(id=int(3))

        return context
