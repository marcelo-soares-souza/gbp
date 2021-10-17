from django.views.generic import DetailView
from ssrnai.models.conyza.conyza_on_targets import Conyza_On_Targets
from ssrnai.models import Database


class BuvaOnTarget(DetailView):
    template_name = 'buva/buva_on_target.html'
    context_object_name = 'ontargets'
    model = Conyza_On_Targets
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(BuvaOnTarget, self).get_context_data(**kwargs)
        context['ontargets'] = Conyza_On_Targets.objects.filter(dsrna=int(self.kwargs['pk']))
        context['database'] = Database.objects.get(id=int(1))

        return context
