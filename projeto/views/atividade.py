from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.db.models import Q
from django.db.models import Count
from django.shortcuts import render

from projeto.forms import AtividadeForm
from projeto.models import Atividade, Projeto
from projeto.views.login import LoggedInMixin


def AtividadeAjax(request, pk):
    atividades = Atividade.objects.filter(projeto_id=int(pk)).order_by('numero')

    return render(request, 'atividades.html', {'atividades': atividades})


def AtividadePlanoAcaoAjax(request, pk):
    atividades = Atividade.objects.filter(planoacao_id=int(pk)).order_by('numero')

    return render(request, 'atividades.html', {'atividades': atividades})


class AtividadeList(LoggedInMixin, ListView):
    allowed_sort_fields = {'nome': {'default_direction': '', 'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 10

    template_name = 'atividade/crud/list.html'
    context_object_name = 'atividades'
    model = Atividade
    fields = '__all__'

    success_url = reverse_lazy('list_atividade_projeto')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(projeto_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(AtividadeList, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        context['projeto_id'] = 0

        if self.kwargs:
            context['projeto_id'] = self.kwargs['pk']

        return context


class AtividadeDetail(LoggedInMixin, DetailView):
    template_name = 'atividade/crud/detail.html'
    context_object_name = 'atividade'
    model = Atividade
    fields = '__all__'

    success_url = reverse_lazy('list_atividade_projeto')


class AtividadeCreate(LoggedInMixin, CreateView):
    template_name = 'atividade/crud/form.html'
    form_class = AtividadeForm

    def get_success_url(self):
        return reverse_lazy('detail_atividade_projeto', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(AtividadeCreate, self).form_valid(form)

    def get_initial(self):
        try:
            return {'criado_por': self.request.user.id, 'numero': int(Atividade.objects.latest('data_atualizado').numero) + 1}
        except Atividade.DoesNotExist:
            return {'criado_por': self.request.user.id}

    def get_context_data(self, **kwargs):
        context = super(AtividadeCreate, self).get_context_data(**kwargs)
        context["projetos"] = Atividade.objects.values('projeto_id').annotate(total=Count('projeto_id')).order_by('projeto_id')

        return context

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(AtividadeCreate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class AtividadeUpdate(LoggedInMixin, UpdateView):
    template_name = 'atividade/crud/form.html'
    form_class = AtividadeForm
    model = Atividade

    def get_success_url(self):
        return reverse_lazy('detail_atividade_projeto', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(AtividadeUpdate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class AtividadeDelete(LoggedInMixin, DeleteView):
    template_name = 'atividade/crud/delete.html'
    model = Atividade
    success_url = reverse_lazy('list_atividade_projeto')
