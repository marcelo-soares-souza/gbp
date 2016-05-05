from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from projeto.models import Projeto
from projeto.forms import ProjetoForm


class ProjetoList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'sigla': {'default_direction': '', 'verbose_name': 'Sigla'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'sigla'
    paginate_by = 5

    template_name = 'projeto/crud/list.html'
    context_object_name = 'projetos'
    model = Projeto
    fields = '__all__'
    success_url = reverse_lazy('list_projeto')


class ProjetoDetail(LoggedInMixin, DetailView):
    template_name = 'projeto/crud/detail.html'
    context_object_name = 'projeto'
    model = Projeto
    fields = '__all__'

    success_url = reverse_lazy('list_projeto')


class ProjetoCreate(LoggedInMixin, CreateView):
    template_name = 'projeto/crud/form.html'
    form_class = ProjetoForm

    success_url = reverse_lazy('new_objetivo_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ProjetoCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}

    def get_context_data(self, **kwargs):
        context = super(ProjetoCreate, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()

        return context


class ProjetoUpdate(LoggedInMixin, UpdateView):
    template_name = 'projeto/crud/form.html'
    form_class = ProjetoForm
    model = Projeto

    success_url = reverse_lazy('new_objetivo_projeto')

    def get_context_data(self, **kwargs):
        context = super(ProjetoUpdate, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()

        return context


class ProjetoDelete(LoggedInMixin, DeleteView):
    template_name = 'projeto/crud/delete.html'
    model = Projeto

    success_url = reverse_lazy('list_projeto')
