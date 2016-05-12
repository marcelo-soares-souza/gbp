from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from projeto.forms import MetaProjetoForm
from projeto.models import MetaProjeto
from projeto.views.login import LoggedInMixin


#
#
# Meta do Projeto
#
#


class MetaProjetoList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'nome': {'default_direction': '',
                                    'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '',
                                               'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 5

    template_name = 'metaprojeto/crud/list.html'
    context_object_name = 'metaprojeto'
    model = MetaProjeto
    fields = '__all__'

    success_url = reverse_lazy('list_metaprojeto_projeto')


class MetaProjetoDetail(LoggedInMixin, DetailView):
    template_name = 'metaprojeto/crud/detail.html'
    context_object_name = 'metaprojeto'
    model = MetaProjeto
    fields = '__all__'

    success_url = reverse_lazy('list_metaprojeto_projeto')


class MetaProjetoCreate(LoggedInMixin, CreateView):
    template_name = 'metaprojeto/crud/form.html'
    form_class = MetaProjetoForm

    success_url = reverse_lazy('list_metaprojeto_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(MetaProjetoCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class MetaProjetoUpdate(LoggedInMixin, UpdateView):
    template_name = 'metaprojeto/crud/form.html'
    form_class = MetaProjetoForm
    model = MetaProjeto

    success_url = reverse_lazy('list_metaprojeto_projeto')


class MetaProjetoDelete(LoggedInMixin, DeleteView):
    template_name = 'metaprojeto/crud/delete.html'
    model = MetaProjeto
    success_url = reverse_lazy('list_metaprojeto_projeto')
