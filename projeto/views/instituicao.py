from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

from projeto.forms import InstituicaoForm
from projeto.models import Instituicao
from projeto.views.login import LoggedInMixin


class InstituicaoProjetoList(LoggedInMixin, ListView):
    allowed_sort_fields = {'nome': {'default_direction': '',
                                    'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '',
                                               'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 10

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

    success_url = reverse_lazy('new_instituicao_projeto')

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
