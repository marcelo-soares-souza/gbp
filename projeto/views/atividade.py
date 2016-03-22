from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from projeto.models import Atividade

#
#
# Atividade
#
#

class AtividadeList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'nome': {'default_direction': '', 'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 5

    template_name = 'atividade/crud/list.html'
    context_object_name = 'atividades'
    model = Atividade
    fields = '__all__'

    success_url = reverse_lazy('list_atividade_projeto')

class AtividadeDetail(LoggedInMixin, DetailView):
    template_name = 'atividade/crud/detail.html'
    context_object_name = 'atividade'
    model = Atividade
    fields = '__all__'

    success_url = reverse_lazy('list_atividade_projeto')

class AtividadeCreate(LoggedInMixin, CreateView):
    template_name = 'atividade/crud/form.html'
    model = Atividade
    fields = ['projeto', 'numero', 'nome', 'indicador_fisico', 'responsavel', 'peso_planoacao', 'data_inicio', 'data_fim', 'colaborador', 'planoacao']

    success_url = reverse_lazy('list_atividade_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(AtividadeCreate, self).form_valid(form)

    def get_initial(self):
        return { 'criado_por': self.request.user.id }

class AtividadeUpdate(LoggedInMixin, UpdateView):
    template_name = 'atividade/crud/form.html'
    model = Atividade
    fields = ['projeto', 'numero', 'nome', 'indicador_fisico', 'responsavel', 'peso_planoacao', 'data_inicio', 'data_fim', 'colaborador', 'planoacao']

    success_url = reverse_lazy('list_atividade_projeto')

class AtividadeDelete(LoggedInMixin, DeleteView):
    template_name = 'atividade/crud/delete.html'
    model = Atividade
    success_url = reverse_lazy('list_atividade_projeto')
