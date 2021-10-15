from django.views.generic import DetailView
from ssrnai.models.capim.capim_off_targets import Capim_Off_Targets

class CapimOffTarget(DetailView):
    template_name = 'capim/capim_on_target.html'
    context_object_name = 'offtargets'
    model = Capim_Off_Targets
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CapimOffTarget, self).get_context_data(**kwargs)
        context['offtargets'] = Capim_Off_Targets.objects.get(gene=int(self.kwargs['pk']))

        return context
