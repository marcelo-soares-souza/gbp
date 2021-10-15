from django.views.generic import DetailView
from ssrnai.models.nematoide.nematoide_off_targets import Nematoide_Off_Targets

class NematoideOffTarget(DetailView):
    template_name = 'nematoide/nematoide_on_target.html'
    context_object_name = 'offtargets'
    model = Nematoide_Off_Targets
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NematoideOffTarget, self).get_context_data(**kwargs)
        context['offtargets'] = Nematoide_Off_Targets.objects.get(gene=int(self.kwargs['pk']))

        return context
