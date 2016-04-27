from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from projeto.models import Status

#
#
# Status de Projeto
#
#


class StatusProjetoList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'nome': {'default_direction': '',
                                    'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '',
                                               'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 5

    template_name = 'status/crud/list.html'
    context_object_name = 'status'
    model = Status
    fields = '__all__'

    success_url = reverse_lazy('list_status_projeto')


class StatusProjetoDetail(LoggedInMixin, DetailView):
    template_name = 'status/crud/detail.html'
    context_object_name = 'status'
    model = Status
    fields = '__all__'

    success_url = reverse_lazy('list_status_projeto')


class StatusProjetoCreate(LoggedInMixin, CreateView):
    template_name = 'status/crud/form.html'
    model = Status
    fields = ['nome']

    success_url = reverse_lazy('list_status_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(StatusProjetoCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class StatusProjetoUpdate(LoggedInMixin, UpdateView):
    template_name = 'status/crud/form.html'
    model = Status
    fields = ['nome']

    success_url = reverse_lazy('list_status_projeto')


class StatusProjetoDelete(LoggedInMixin, DeleteView):
    template_name = 'status/crud/delete.html'
    model = Status
    success_url = reverse_lazy('list_status_projeto')
