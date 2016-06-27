from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView

from projeto.views.login import LoggedInMixin
from sequenciamento.models import Sequenciamento


class DashboardList(LoggedInMixin, ListView):
    template_name = 'dashboard/crud/detail.html'
    context_object_name = 'sequenciamentos'
    model = Sequenciamento
    fields = '__all__'

    success_url = reverse_lazy('dashboard_sequenciamento')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(DashboardList, self).get_context_data(**kwargs)
        context['sequenciamentos_list'] = Sequenciamento.objects.all()
        context['sequenciamento_id'] = 0

        if self.kwargs:
            context['sequenciamento_id'] = self.kwargs['pk']

        return context
