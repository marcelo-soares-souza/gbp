from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from sequenciamento.models import Sequenciamento
from sequenciamento.forms import SequenciamentoForm


class SequenciamentoList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'material_biologico': {'default_direction': '',
                                                  'verbose_name': 'Matérial Biológico'},
                           'data_atualizado': {'default_direction': '',
                                               'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'material_biologico'
    paginate_by = 5

    template_name = 'sequenciamento/crud/list.html'
    context_object_name = 'sequenciamentos'
    model = Sequenciamento
    fields = '__all__'

    success_url = reverse_lazy('list_sequenciamento')


class SequenciamentoDetail(LoggedInMixin, DetailView):
    template_name = 'sequenciamento/crud/detail.html'
    context_object_name = 'sequenciamento'
    model = Sequenciamento
    fields = '__all__'

    success_url = reverse_lazy('list_sequenciamento')


class SequenciamentoCreate(LoggedInMixin, CreateView):
    template_name = 'sequenciamento/crud/form.html'
    form_class = SequenciamentoForm

    success_url = reverse_lazy('new_sequenciamento')

    def get_context_data(self, **kwargs):
        context = super(SequenciamentoCreate,
                        self).get_context_data(**kwargs)
        context["sequenciamentos"] = Sequenciamento.objects.all(
        ).order_by('material_biologico')
        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(SequenciamentoCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class SequenciamentoUpdate(LoggedInMixin, UpdateView):
    template_name = 'sequenciamento/crud/form.html'
    form_class = SequenciamentoForm
    model = Sequenciamento

    success_url = reverse_lazy('new_sequenciamento')

    def get_context_data(self, **kwargs):
        context = super(SequenciamentoUpdate,
                        self).get_context_data(**kwargs)
        context["sequenciamentos"] = Sequenciamento.objects.all(
        ).order_by('material_biologico')
        return context


class SequenciamentoDelete(LoggedInMixin, DeleteView):
    template_name = 'sequenciamento/crud/delete.html'
    model = Sequenciamento
    success_url = reverse_lazy('new_sequenciamento')
