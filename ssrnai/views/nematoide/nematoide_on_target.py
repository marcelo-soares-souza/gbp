from django.views.generic import DetailView
from ssrnai.models.nematoide.nematoide_on_targets import Nematoide_On_Targets
from ssrnai.models import Database


class NematoideOnTarget(DetailView):
    template_name = 'nematoide/nematoide_on_target.html'
    context_object_name = 'ontargets'
    model = Nematoide_On_Targets
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NematoideOnTarget, self).get_context_data(**kwargs)
        context['ontargets'] = Nematoide_On_Targets.objects.filter(dsrna=int(self.kwargs['pk']))
        context['database'] = Database.objects.get(id=int(3))

        return context
