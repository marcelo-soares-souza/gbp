from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from projeto.models import Tarefa

#
#
# Tarefas
#
#

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

class TarefaDetail(LoggedInMixin, DetailView):
    template_name = 'tarefa/crud/detail.html'
    context_object_name = 'tarefa'
    model = Tarefa
    fields = '__all__'

    success_url = reverse_lazy('list_tarefa_projeto')

class TarefaCreate(LoggedInMixin, CreateView):
    template_name = 'tarefa/crud/form.html'
    model = Tarefa
    fields = ['projeto', 'planoacao','atividade', 'numero', 'nome', 'indicador_fisico', 'responsavel', 'peso_atividade', 'colaborador']

    success_url = reverse_lazy('list_tarefa_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(TarefaCreate, self).form_valid(form)

    def get_initial(self):
        return { 'criado_por': self.request.user.id }

class TarefaUpdate(LoggedInMixin, UpdateView):
    template_name = 'tarefa/crud/form.html'
    model = Tarefa
    fields = ['projeto', 'planoacao', 'atividade', 'numero', 'nome', 'indicador_fisico', 'responsavel', 'peso_atividade', 'colaborador']

    success_url = reverse_lazy('list_tarefa_projeto')

class TarefaDelete(LoggedInMixin, DeleteView):
    template_name = 'tarefa/crud/delete.html'
    model = Tarefa
    success_url = reverse_lazy('list_tarefa_projeto')
