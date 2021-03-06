from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.db.models import Q
from django.db.models import Count
from django.shortcuts import render

from projeto.forms import TarefaForm
from projeto.models import Tarefa, Projeto
from projeto.views.login import LoggedInMixin


def TarefaAjax(request, pk):
    tarefas = Tarefa.objects.filter(projeto_id=int(pk)).order_by('numero')

    return render(request, 'tarefas.html', {'tarefas': tarefas})


def TarefaPlanoAcaoAjax(request, pk):
    tarefas = Tarefa.objects.filter(planoacao_id=int(pk)).order_by('numero')

    return render(request, 'tarefas.html', {'tarefas': tarefas})


class TarefaList(LoggedInMixin, ListView):
    allowed_sort_fields = {'nome': {'default_direction': '', 'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 10

    template_name = 'tarefa/crud/list.html'
    context_object_name = 'tarefas'
    model = Tarefa
    fields = '__all__'

    success_url = reverse_lazy('list_tarefa_projeto')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(projeto_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(TarefaList, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        context['projeto_id'] = 0

        if self.kwargs:
            context['projeto_id'] = self.kwargs['pk']

        return context


class TarefaDetail(LoggedInMixin, DetailView):
    template_name = 'tarefa/crud/detail.html'
    context_object_name = 'tarefa'
    model = Tarefa
    fields = '__all__'

    success_url = reverse_lazy('list_tarefa_projeto')


class TarefaCreate(LoggedInMixin, CreateView):
    template_name = 'tarefa/crud/form.html'
    form_class = TarefaForm

    def get_success_url(self):
        return reverse_lazy('detail_tarefa_projeto', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(TarefaCreate, self).form_valid(form)

    def get_initial(self):
        try:
            return {'criado_por': self.request.user.id, 'numero': int(Tarefa.objects.latest('data_atualizado').numero) + 1}
        except Tarefa.DoesNotExist:
            return {'criado_por': self.request.user.id}

    def get_context_data(self, **kwargs):
        context = super(TarefaCreate, self).get_context_data(**kwargs)
        context["projetos"] = Tarefa.objects.values('projeto_id').annotate(total=Count('projeto_id')).order_by('projeto_id')

        return context

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(TarefaCreate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class TarefaUpdate(LoggedInMixin, UpdateView):
    template_name = 'tarefa/crud/form.html'
    form_class = TarefaForm
    model = Tarefa

    def get_success_url(self):
        return reverse_lazy('detail_tarefa_projeto', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(TarefaUpdate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class TarefaDelete(LoggedInMixin, DeleteView):
    template_name = 'tarefa/crud/delete.html'
    model = Tarefa
    success_url = reverse_lazy('list_tarefa_projeto')
