from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView
from django.db.models import Count
from django.shortcuts import render

from projeto.forms import TarefaForm
from projeto.models import Tarefa, Projeto
from projeto.views.login import LoggedInMixin


def TarefaAjax(request, pk):
    tarefas = Tarefa.objects.filter(projeto_id=int(pk)).order_by('numero')

    return render(request, 'tarefas.html', {'tarefas': tarefas})


def TarefaPlanoAcaoAjax(request, pk):
    tarefas = Tarefa.objects.filter(planoacao_id=int(pk)).order_by('numero')

    return render(request, 'tarefas.html', {'tarefas': tarefas})


class TarefaList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'nome': {'default_direction': '', 'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 5

    template_name = 'tarefa/crud/list.html'
    context_object_name = 'tarefas'
    model = Tarefa
    fields = '__all__'

    success_url = reverse_lazy('list_tarefa_projeto')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(projeto_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(TarefaList, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        context['projeto_id'] = 0

        if self.kwargs:
            context['projeto_id'] = self.kwargs['pk']

        return context


class TarefaDetail(LoggedInMixin, DetailView):
    template_name = 'tarefa/crud/detail.html'
    context_object_name = 'tarefa'
    model = Tarefa
    fields = '__all__'

    success_url = reverse_lazy('list_tarefa_projeto')


class TarefaCreate(LoggedInMixin, CreateView):
    template_name = 'tarefa/crud/form.html'
    form_class = TarefaForm

    success_url = reverse_lazy('list_tarefa_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(TarefaCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}

    def get_context_data(self, **kwargs):
        context = super(TarefaCreate, self).get_context_data(**kwargs)
        context["projetos"] = Tarefa.objects.values('projeto_id').annotate(total=Count('projeto_id')).order_by('projeto_id')

        return context


class TarefaUpdate(LoggedInMixin, UpdateView):
    template_name = 'tarefa/crud/form.html'
    form_class = TarefaForm
    model = Tarefa

    success_url = reverse_lazy('list_tarefa_projeto')


class TarefaDelete(LoggedInMixin, DeleteView):
    template_name = 'tarefa/crud/delete.html'
    model = Tarefa
    success_url = reverse_lazy('list_tarefa_projeto')
