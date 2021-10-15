from django.views.generic import DetailView
from ssrnai.models.lagarta.lagarta_off_targets import Lagarta_Off_Targets

class LagartaOffTarget(DetailView):
    template_name = 'lagarta/lagarta_on_target.html'
    context_object_name = 'offtargets'
    model = Lagarta_Off_Targets
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(LagartaOffTarget, self).get_context_data(**kwargs)
        context['offtargets'] = Lagarta_Off_Targets.objects.get(gene=int(self.kwargs['pk']))

        return context
