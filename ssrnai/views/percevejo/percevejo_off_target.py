from django.views.generic import DetailView
from ssrnai.models.percevejo.percevejo_off_targets import Percevejo_Off_Targets
from ssrnai.models import Database

class PercevejoOffTarget(DetailView):
    template_name = 'percevejo/percevejo_on_target.html'
    context_object_name = 'offtargets'
    model = Percevejo_Off_Targets
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PercevejoOffTarget, self).get_context_data(**kwargs)
        context['offtargets'] = Percevejo_Off_Targets.objects.get(gene=int(self.kwargs['pk']))
        context['database'] = Database.objects.get(id=int(5))

        return context
