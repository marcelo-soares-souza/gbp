from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin, CreatedByRequiredMixin, ColaboradorRequiredMixin, ListColaboradorRequiredMixin
from sequenciamento.models import TipoSequenciamento
from sequenciamento.forms import TipoSequenciamentoForm


class TipoSequenciamentoList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'nome': {'default_direction': '',
                                    'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '',
                                               'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 5

    template_name = 'tiposequenciamento/crud/list.html'
    context_object_name = 'tiposequenciamentos'
    model = TipoSequenciamento
    fields = '__all__'

    success_url = reverse_lazy('list_tiposequenciamento')


class TipoSequenciamentoDetail(LoggedInMixin, DetailView):
    template_name = 'tiposequenciamento/crud/detail.html'
    context_object_name = 'tiposequenciamento'
    model = TipoSequenciamento
    fields = '__all__'

    success_url = reverse_lazy('list_tiposequenciamento')


class TipoSequenciamentoCreate(LoggedInMixin, CreateView):
    template_name = 'tiposequenciamento/crud/form.html'
    form_class = TipoSequenciamentoForm

    success_url = reverse_lazy('list_tiposequenciamento')

    def get_context_data(self, **kwargs):
        context = super(TipoSequenciamentoCreate,
                        self).get_context_data(**kwargs)
        context["tiposequenciamentos"] = TipoSequenciamento.objects.all(
        ).order_by('nome')
        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(TipoSequenciamentoCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class TipoSequenciamentoUpdate(LoggedInMixin, CreatedByRequiredMixin, UpdateView):
    template_name = 'tiposequenciamento/crud/form.html'
    form_class = TipoSequenciamentoForm
    model = TipoSequenciamento

    success_url = reverse_lazy('list_tiposequenciamento')

    def get_context_data(self, **kwargs):
        context = super(TipoSequenciamentoUpdate,
                        self).get_context_data(**kwargs)
        context["tiposequenciamentos"] = TipoSequenciamento.objects.all(
        ).order_by('nome')
        return context


class TipoSequenciamentoDelete(LoggedInMixin, CreatedByRequiredMixin, DeleteView):
    template_name = 'tiposequenciamento/crud/delete.html'
    model = TipoSequenciamento
    success_url = reverse_lazy('list_tiposequenciamento')
