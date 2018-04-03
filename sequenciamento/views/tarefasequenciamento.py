from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

from projeto.views.login import CreatedByRequiredMixin, ListResponsavelRequiredMixin, LoggedInMixin, ResponsavelRequiredMixin
from sequenciamento.forms import TarefaSequenciamentoForm
from sequenciamento.models import Sequenciamento, TarefaSequenciamento

# import logging
# logger = logging.getLogger('sequenciamento')


class TarefaSequenciamentoList(LoggedInMixin, ListResponsavelRequiredMixin, ListView):
    allowed_sort_fields = {'tarefa': {'default_direction': '', 'verbose_name': 'Tarefa'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'tarefa'
    paginate_by = 10

    template_name = 'tarefasequenciamento/crud/list.html'
    context_object_name = 'tarefasequenciamentos'
    model = TarefaSequenciamento
    fields = '__all__'

    success_url = reverse_lazy('list_tarefasequenciamento')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(sequenciamento_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(TarefaSequenciamentoList, self).get_context_data(**kwargs)
        context['sequenciamentos'] = Sequenciamento.objects.all()
        context['sequenciamento_id'] = 0

        if self.kwargs:
            context['sequenciamento_id'] = self.kwargs['pk']

        return context


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
        data = {'criado_por': self.request.user.id}

        if self.kwargs:
            data['sequenciamento'] = int(self.kwargs['pk'])

        return data


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
