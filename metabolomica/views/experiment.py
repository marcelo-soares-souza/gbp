from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from metabolomica.forms import ExperimentForm
from metabolomica.models import Experiment
from projeto.views.login import LoggedInMixin


class ExperimentList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {
                  'name':
                  {'default_direction': '', 'verbose_name': 'Name'},
                  'data_atualizado':
                  {'default_direction': '', 'verbose_name': 'Modified'}
                           }  # Atualizado Em Modified

    default_sort_field = 'name'
    paginate_by = 5

    template_name = 'experiment/crud/list.html'
    context_object_name = 'experiments'
    model = Experiment
    fields = '__all__'

    success_url = reverse_lazy('list_experiment')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(
                                   metabolomica_id=int(self.kwargs['pk'])
                                                          )
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ExperimentList, self).get_context_data(**kwargs)
        context['metabolomicas'] = Experiment.objects.all()
        context['metabolomica_id'] = 0

        if self.kwargs:
            context['metabolomica_id'] = self.kwargs['pk']

        return context


class ExperimentDetail(LoggedInMixin, DetailView):
    template_name = 'experiment/crud/detail.html'
    context_object_name = 'experiment'
    model = Experiment
    fields = '__all__'

    success_url = reverse_lazy('list_experiment')


class ExperimentCreate(LoggedInMixin, CreateView):
    template_name = 'experiment/crud/form.html'
    form_class = ExperimentForm
    success_url = reverse_lazy('list_experiment')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ExperimentCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class ExperimentUpdate(LoggedInMixin, UpdateView):
    template_name = 'experiment/crud/form.html'
    form_class = ExperimentForm
    model = Experiment

    def get_context_data(self, **kwargs):
        context = super(ExperimentUpdate, self).get_context_data(**kwargs)
        context["experiments"] = Experiment.objects.all().order_by('numero')
        return context

    success_url = reverse_lazy('list_experiment')


class ExperimentDelete(LoggedInMixin, DeleteView):
    template_name = 'experiment/crud/delete.html'
    model = Experiment
    success_url = reverse_lazy('list_experiment')
