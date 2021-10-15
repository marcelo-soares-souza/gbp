from django.views.generic import DetailView
from ssrnai.models.nematoide.nematoide_on_targets import Nematoide_On_Targets


class NematoideOnTarget(DetailView):
    template_name = 'nematoide/nematoide_on_target.html'
    context_object_name = 'ontargets'
    model = Nematoide_On_Targets
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NematoideOnTarget, self).get_context_data(**kwargs)
        context['ontargets'] = Nematoide_On_Targets.objects.filter(dsrna=int(self.kwargs['pk']))

        return context
