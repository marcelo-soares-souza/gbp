from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.db.models import Q
from django.db.models import Count
from django.shortcuts import render

from projeto.forms import PlanoAcaoForm
from projeto.models import PlanoAcao, Projeto
from projeto.views.login import LoggedInMixin


def PlanoAcaoAjax(request, pk):
    planoacaos = PlanoAcao.objects.filter(projeto_id=int(pk)).order_by('numero')

    return render(request, 'planoacaos.html', {'planoacaos': planoacaos})


def PlanoAcaoProjetoComponenteAjax(request, pk):
    planoacaos = PlanoAcao.objects.filter(projeto_componente_id=int(pk)).order_by('numero')

    return render(request, 'planoacaos.html', {'planoacaos': planoacaos})


class PlanoAcaoList(LoggedInMixin, ListView):
    allowed_sort_fields = {'nome': {'default_direction': '', 'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 10

    template_name = 'planoacao/crud/list.html'
    context_object_name = 'planosacao'
    model = PlanoAcao
    fields = '__all__'

    success_url = reverse_lazy('list_planoacao_projeto')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(projeto_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(PlanoAcaoList, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        context['projeto_id'] = 0

        if self.kwargs:
            context['projeto_id'] = self.kwargs['pk']

        return context


class PlanoAcaoDetail(LoggedInMixin, DetailView):
    template_name = 'planoacao/crud/detail.html'
    context_object_name = 'planoacao'
    model = PlanoAcao
    fields = '__all__'

    success_url = reverse_lazy('list_planoacao_projeto')


class PlanoAcaoCreate(LoggedInMixin, CreateView):
    template_name = 'planoacao/crud/form.html'
    form_class = PlanoAcaoForm

    def get_success_url(self):
        return reverse_lazy('detail_planoacao_projeto', kwargs={'pk' : self.object.pk})

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(PlanoAcaoCreate, self).form_valid(form)

    def get_initial(self):
        try:
            return {'criado_por': self.request.user.id, 'numero': int(PlanoAcao.objects.latest('data_atualizado').numero) + 1}
        except PlanoAcao.DoesNotExist:
            return {'criado_por': self.request.user.id}

    def get_context_data(self, **kwargs):
        context = super(PlanoAcaoCreate, self).get_context_data(**kwargs)
        context["projetos"] = PlanoAcao.objects.values('projeto_id').annotate(total=Count('projeto_id')).order_by('projeto_id')

        return context

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(PlanoAcaoCreate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class PlanoAcaoUpdate(LoggedInMixin, UpdateView):
    template_name = 'planoacao/crud/form.html'
    form_class = PlanoAcaoForm
    model = PlanoAcao

    def get_success_url(self):
        return reverse_lazy('detail_planoacao_projeto', kwargs={'pk' : self.object.pk})

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(PlanoAcaoUpdate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class PlanoAcaoDelete(LoggedInMixin, DeleteView):
    template_name = 'planoacao/crud/delete.html'
    model = PlanoAcao
    success_url = reverse_lazy('list_planoacao_projeto')
