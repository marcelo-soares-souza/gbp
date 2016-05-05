from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from projeto.models import Tipo

#
#
# Tipo de Projeto
#
#


class TipoProjetoList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'sigla': {'default_direction': '',
                                     'verbose_name': 'Sigla'},
                           'data_atualizado': {'default_direction': '',
                                               'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'sigla'
    paginate_by = 5

    template_name = 'tipo/crud/list.html'
    context_object_name = 'tipos'
    model = Tipo
    fields = '__all__'

    success_url = reverse_lazy('list_tipo_projeto')


class TipoProjetoDetail(LoggedInMixin, DetailView):
    template_name = 'tipo/crud/detail.html'
    context_object_name = 'tipo'
    model = Tipo
    fields = '__all__'

    success_url = reverse_lazy('list_tipo_projeto')


class TipoProjetoCreate(LoggedInMixin, CreateView):
    template_name = 'tipo/crud/form.html'
    model = Tipo
    fields = ['sigla']

    success_url = reverse_lazy('list_tipo_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(TipoProjetoCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class TipoProjetoUpdate(LoggedInMixin, UpdateView):
    template_name = 'tipo/crud/form.html'
    model = Tipo
    fields = ['sigla']

    success_url = reverse_lazy('list_tipo_projeto')


class TipoProjetoDelete(LoggedInMixin, DeleteView):
    template_name = 'tipo/crud/delete.html'
    model = Tipo
    success_url = reverse_lazy('list_tipo_projeto')
