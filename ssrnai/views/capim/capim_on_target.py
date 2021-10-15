from django.views.generic import DetailView
from ssrnai.models.capim.capim_on_targets import Capim_On_Targets

class CapimOnTarget(DetailView):
    template_name = 'capim/capim_on_target.html'
    context_object_name = 'ontargets'
    model = Capim_On_Targets
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CapimOnTarget, self).get_context_data(**kwargs)
        context['ontargets'] = Capim_On_Targets.objects.filter(dsrna=int(self.kwargs['pk']))

        return context
