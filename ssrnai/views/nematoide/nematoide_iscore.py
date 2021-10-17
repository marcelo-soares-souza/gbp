from django.views.generic import DetailView
from ssrnai.models.nematoide.nematoide_iscore import Nematoide_Iscore
from ssrnai.models.nematoide.nematoide_gene_information import Nematoide_Gene_Information
from ssrnai.models.nematoide.nematoide_dsrna_information import Nematoide_Dsrna_Information
from ssrnai.models import Database

class NematoideIScore(DetailView):
    template_name = 'nematoide/nematoide_iscore.html'
    context_object_name = 'iscore'
    model = Nematoide_Iscore
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NematoideIScore, self).get_context_data(**kwargs)
        context['iscore'] = Nematoide_Iscore.objects.get(id=int(self.kwargs['pk']))
        iscore = context['iscore']
        context['dsRNA'] = Nematoide_Dsrna_Information.objects.get(id=int(iscore.dsrna_id))
        context['gene'] = Nematoide_Gene_Information.objects.get(id=int(iscore.gene_id))
        context['database'] = Database.objects.get(id=int(3))

        return context
