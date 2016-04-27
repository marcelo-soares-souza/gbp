from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from projeto.models import ProjetoComponente
from projeto.forms import ProjetoComponenteForm

#
#
# Projeto Componente
#
#


class ProjetoComponenteList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'nome': {'default_direction': '', 'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 5

    template_name = 'projetocomponente/crud/list.html'
    context_object_name = 'projetoscomponentes'
    model = ProjetoComponente
    fields = '__all__'

    success_url = reverse_lazy('list_projetocomponente_projeto')


class ProjetoComponenteDetail(LoggedInMixin, DetailView):
    template_name = 'projetocomponente/crud/detail.html'
    context_object_name = 'projetocomponente'
    model = ProjetoComponente
    fields = '__all__'

    success_url = reverse_lazy('list_projetocomponente_projeto')


class ProjetoComponenteCreate(LoggedInMixin, CreateView):
    template_name = 'projetocomponente/crud/form.html'
    form_class = ProjetoComponenteForm

    success_url = reverse_lazy('list_projetocomponente_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ProjetoComponenteCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class ProjetoComponenteUpdate(LoggedInMixin, UpdateView):
    template_name = 'projetocomponente/crud/form.html'
    form_class = ProjetoComponenteForm
    model = ProjetoComponente

    success_url = reverse_lazy('list_projetocomponente_projeto')


class ProjetoComponenteDelete(LoggedInMixin, DeleteView):
    template_name = 'projetocomponente/crud/delete.html'
    model = ProjetoComponente
    success_url = reverse_lazy('list_projetocomponente_projeto')
