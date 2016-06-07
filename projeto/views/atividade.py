from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from projeto.forms import AtividadeForm
from projeto.models import Atividade, Projeto
from projeto.views.login import LoggedInMixin


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

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(projeto_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(AtividadeList, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        context['projeto_id'] = 0

        if self.kwargs:
            context['projeto_id'] = self.kwargs['pk']

        return context


class AtividadeDetail(LoggedInMixin, DetailView):
    template_name = 'atividade/crud/detail.html'
    context_object_name = 'atividade'
    model = Atividade
    fields = '__all__'

    success_url = reverse_lazy('list_atividade_projeto')


class AtividadeCreate(LoggedInMixin, CreateView):
    template_name = 'atividade/crud/form.html'
    form_class = AtividadeForm

    success_url = reverse_lazy('list_atividade_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(AtividadeCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class AtividadeUpdate(LoggedInMixin, UpdateView):
    template_name = 'atividade/crud/form.html'
    form_class = AtividadeForm
    model = Atividade

    success_url = reverse_lazy('list_atividade_projeto')


class AtividadeDelete(LoggedInMixin, DeleteView):
    template_name = 'atividade/crud/delete.html'
    model = Atividade
    success_url = reverse_lazy('list_atividade_projeto')
