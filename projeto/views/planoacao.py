from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from projeto.models import PlanoAcao
from projeto.forms import PlanoAcaoForm
#
#
# Plano de Ação
#
#

class PlanoAcaoList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'nome': {'default_direction': '', 'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 5

    template_name = 'planoacao/crud/list.html'
    context_object_name = 'planosacao'
    model = PlanoAcao
    fields = '__all__'

    success_url = reverse_lazy('list_planoacao_projeto')

class PlanoAcaoDetail(LoggedInMixin, DetailView):
    template_name = 'planoacao/crud/detail.html'
    context_object_name = 'planoacao'
    model = PlanoAcao
    fields = '__all__'

    success_url = reverse_lazy('list_planoacao_projeto')

class PlanoAcaoCreate(LoggedInMixin, CreateView):
    template_name = 'planoacao/crud/form.html'
    form_class = PlanoAcaoForm

    success_url = reverse_lazy('list_planoacao_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(PlanoAcaoCreate, self).form_valid(form)

    def get_initial(self):
        return { 'criado_por': self.request.user.id }

class PlanoAcaoUpdate(LoggedInMixin, UpdateView):
    template_name = 'planoacao/crud/form.html'
    form_class = PlanoAcaoForm
    model = PlanoAcao

    success_url = reverse_lazy('list_planoacao_projeto')

class PlanoAcaoDelete(LoggedInMixin, DeleteView):
    template_name = 'planoacao/crud/delete.html'
    model = PlanoAcao
    success_url = reverse_lazy('list_planoacao_projeto')
