from django.views.generic import DetailView
from ssrnai.models.lagarta.lagarta_on_targets import Lagarta_On_Targets
from ssrnai.models import Database

class LagartaOnTarget(DetailView):
    template_name = 'lagarta/lagarta_on_target.html'
    context_object_name = 'ontargets'
    model = Lagarta_On_Targets
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(LagartaOnTarget, self).get_context_data(**kwargs)
        context['ontargets'] = Lagarta_On_Targets.objects.filter(dsrna=int(self.kwargs['pk']))
        context['database'] = Database.objects.get(id=int(4))

        return context
