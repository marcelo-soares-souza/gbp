from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from projeto.models import Instituicao
from projeto.forms import InstituicaoForm

#
#
# Instituicao de Projeto
#
#


class InstituicaoProjetoList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'nome': {'default_direction': '',
                                    'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '',
                                               'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 5

    template_name = 'instituicao/crud/list.html'
    context_object_name = 'instituicaos'
    model = Instituicao
    fields = '__all__'

    success_url = reverse_lazy('list_instituicao_projeto')


class InstituicaoProjetoDetail(LoggedInMixin, DetailView):
    template_name = 'instituicao/crud/detail.html'
    context_object_name = 'instituicao'
    model = Instituicao
    fields = '__all__'

    success_url = reverse_lazy('list_instituicao_projeto')


class InstituicaoProjetoCreate(LoggedInMixin, CreateView):
    template_name = 'instituicao/crud/form.html'
    form_class = InstituicaoForm
    success_url = reverse_lazy('list_instituicao_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(InstituicaoProjetoCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class InstituicaoProjetoUpdate(LoggedInMixin, UpdateView):
    template_name = 'instituicao/crud/form.html'
    form_class = InstituicaoForm
    model = Instituicao

    success_url = reverse_lazy('list_instituicao_projeto')


class InstituicaoProjetoDelete(LoggedInMixin, DeleteView):
    template_name = 'instituicao/crud/delete.html'
    model = Instituicao
    success_url = reverse_lazy('list_instituicao_projeto')
