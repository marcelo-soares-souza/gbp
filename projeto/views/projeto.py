from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.db.models import Q
from projeto.forms import ProjetoForm
from projeto.models import Projeto
from projeto.views.login import LoggedInMixin


class ProjetoList(LoggedInMixin, ListView):
    allowed_sort_fields = {'sigla': {'default_direction': '', 'verbose_name': 'Sigla'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'sigla'
    paginate_by = 10

    template_name = 'projeto/crud/list.html'
    context_object_name = 'projetos'
    model = Projeto
    fields = '__all__'
    success_url = reverse_lazy('list_projeto')

    def get_context_data(self, **kwargs):
        context = super(ProjetoList, self).get_context_data(**kwargs)

        if self.request.user.is_superuser:
            context['projetos'] = Projeto.objects.all()
        else:
            context['projetos'] = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        query = self.request.GET.get('q')

        if query:
            context['projetos'] = context['projetos'].filter(Q(titulo_portugues__icontains=query) | Q(sigla__icontains=query))
            context['projetos'] = context['projetos'].distinct()

        return context


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

        if self.request.user.is_superuser:
            context['projetos'] = Projeto.objects.all()
        else:
            context['projetos'] = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        return context


class ProjetoUpdate(LoggedInMixin, UpdateView):
    template_name = 'projeto/crud/form.html'
    form_class = ProjetoForm
    model = Projeto

    success_url = reverse_lazy('new_objetivo_projeto')

    def get_context_data(self, **kwargs):
        context = super(ProjetoUpdate, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['projetos'] = Projeto.objects.all()
        else:
            context['projetos'] = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        return context


class ProjetoDelete(LoggedInMixin, DeleteView):
    template_name = 'projeto/crud/delete.html'
    model = Projeto

    success_url = reverse_lazy('list_projeto')
