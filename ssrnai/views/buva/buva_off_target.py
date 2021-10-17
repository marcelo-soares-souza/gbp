from django.views.generic import DetailView
from ssrnai.models.conyza.conyza_off_targets import Conyza_Off_Targets
from ssrnai.models import Database


class BuvaOffTarget(DetailView):
    template_name = 'buva/buva_on_target.html'
    context_object_name = 'offtargets'
    model = Conyza_Off_Targets
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(BuvaOffTarget, self).get_context_data(**kwargs)
        context['offtargets'] = Conyza_Off_Targets.objects.get(gene=int(self.kwargs['pk']))
        context['database'] = Database.objects.get(id=int(1))

        return context
