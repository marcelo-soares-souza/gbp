from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from projeto.views.login import ColaboradorRequiredMixin, ListColaboradorRequiredMixin, LoggedInMixin
from sequenciamento.forms import SequenciamentoForm
from sequenciamento.models import Sequenciamento, TipoSequenciamento


class SequenciamentoList(LoggedInMixin, ListColaboradorRequiredMixin, SortableListView):
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

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(tipo_sequenciamento_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(SequenciamentoList, self).get_context_data(**kwargs)
        context['tipos'] = TipoSequenciamento.objects.all()
        context['tipo_id'] = 0

        if self.kwargs:
            context['tipo_id'] = self.kwargs['pk']

        return context


class SequenciamentoDetail(LoggedInMixin, ColaboradorRequiredMixin, DetailView):
    permission_required = 'sequenciamento.change_userprofile'
    template_name = 'sequenciamento/crud/detail.html'
    context_object_name = 'sequenciamento'
    model = Sequenciamento
    fields = '__all__'

    success_url = reverse_lazy('list_sequenciamento')


class SequenciamentoCreate(LoggedInMixin, CreateView):
    template_name = 'sequenciamento/crud/form.html'
    form_class = SequenciamentoForm

    success_url = reverse_lazy('list_sequenciamento')

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
        data = {'criado_por': self.request.user.id, 'responsavel': self.request.user.id}

        if self.kwargs:
            data['tipo_sequenciamento'] = int(self.kwargs['pk'])

        return data


class SequenciamentoUpdate(LoggedInMixin, ColaboradorRequiredMixin, UpdateView):
    template_name = 'sequenciamento/crud/form.html'
    form_class = SequenciamentoForm
    model = Sequenciamento

    success_url = reverse_lazy('list_sequenciamento')


class SequenciamentoDelete(LoggedInMixin, ColaboradorRequiredMixin, DeleteView):
    template_name = 'sequenciamento/crud/delete.html'
    model = Sequenciamento
    success_url = reverse_lazy('list_sequenciamento')
