from django.views.generic import DetailView
from ssrnai.models.percevejo.percevejo_on_targets import Percevejo_On_Targets
from ssrnai.models import Database


class PercevejoOnTarget(DetailView):
    template_name = 'percevejo/percevejo_on_target_.html'
    context_object_name = 'ontargets'
    model = Percevejo_On_Targets
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PercevejoOnTarget, self).get_context_data(**kwargs)
        context['ontargets'] = Percevejo_On_Targets.objects.filter(dsrna=int(self.kwargs['pk']))
        context['database'] = Database.objects.get(id=int(5))

        return context
