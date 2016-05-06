from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin, CreatedByRequiredMixin, ListResponsavelRequiredMixin, ResponsavelRequiredMixin
from sequenciamento.models import TarefaSequenciamento
from sequenciamento.forms import TarefaSequenciamentoForm


class TarefaSequenciamentoList(LoggedInMixin, ListResponsavelRequiredMixin, SortableListView):
    allowed_sort_fields = {'tarefa': {'default_direction': '', 'verbose_name': 'Tarefa'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'tarefa'
    paginate_by = 5

    template_name = 'tarefasequenciamento/crud/list.html'
    context_object_name = 'tarefasequenciamentos'
    model = TarefaSequenciamento
    fields = '__all__'

    success_url = reverse_lazy('list_tarefasequenciamento')


class TarefaSequenciamentoDetail(LoggedInMixin, ResponsavelRequiredMixin, DetailView):
    template_name = 'tarefasequenciamento/crud/detail.html'
    context_object_name = 'tarefasequenciamento'
    model = TarefaSequenciamento
    fields = '__all__'

    success_url = reverse_lazy('list_tarefasequenciamento')


class TarefaSequenciamentoCreate(LoggedInMixin, CreateView):
    template_name = 'tarefasequenciamento/crud/form.html'
    form_class = TarefaSequenciamentoForm

    success_url = reverse_lazy('list_tarefasequenciamento')

    def get_context_data(self, **kwargs):
        context = super(TarefaSequenciamentoCreate,
                        self).get_context_data(**kwargs)
        context["tarefasequenciamentos"] = TarefaSequenciamento.objects.all().order_by('tarefa')
        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(TarefaSequenciamentoCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class TarefaSequenciamentoUpdate(LoggedInMixin, ResponsavelRequiredMixin, UpdateView):
    template_name = 'tarefasequenciamento/crud/form.html'
    form_class = TarefaSequenciamentoForm
    model = TarefaSequenciamento

    success_url = reverse_lazy('list_tarefasequenciamento')

    def get_context_data(self, **kwargs):
        context = super(TarefaSequenciamentoUpdate,
                        self).get_context_data(**kwargs)
        context["tarefasequenciamentos"] = TarefaSequenciamento.objects.all().order_by('tarefa')
        return context


class TarefaSequenciamentoDelete(LoggedInMixin, CreatedByRequiredMixin, DeleteView):
    template_name = 'tarefasequenciamento/crud/delete.html'
    model = TarefaSequenciamento
    success_url = reverse_lazy('list_tarefasequenciamento')
