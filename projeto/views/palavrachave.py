from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from projeto.models import PalavraChave


#
# View de PalavraChave - métodos
#

class PalavraChaveList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'palavra': {'default_direction': '', 'verbose_name': 'Palavra'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'palavra'
    paginate_by = 5

    template_name = 'palavrachave/crud/list.html'
    context_object_name = 'palavraschaves'
    model = PalavraChave
    fields = '__all__'

    success_url = reverse_lazy('list_palavrachave_projeto')

class PalavraChaveDetail(LoggedInMixin, DetailView):
    template_name = 'palavrachave/crud/detail.html'
    context_object_name = 'palavrachave'
    model = PalavraChave
    fields = '__all__'

    success_url = reverse_lazy('list_palavrachave_projeto')
    
class PalavraChaveCreate(LoggedInMixin, CreateView):
    template_name = 'palavrachave/crud/form.html'
    model = PalavraChave
    fields = ['palavra']

    success_url = reverse_lazy('list_palavrachave_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(PalavraChaveCreate, self).form_valid(form)

    def get_initial(self):
        return { 'criado_por': self.request.user.id }
        
class PalavraChaveUpdate(LoggedInMixin, UpdateView):
    template_name = 'palavrachave/crud/form.html'
    model = PalavraChave
    fields = ['palavra']

    success_url = reverse_lazy('list_palavrachave_projeto')
    
class PalavraChaveDelete(LoggedInMixin, DeleteView):
    template_name = 'palavrachave/crud/delete.html'
    model = PalavraChave
    success_url = reverse_lazy('list_palavrachave_projeto')
