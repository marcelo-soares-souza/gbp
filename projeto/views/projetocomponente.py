from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

from django.db.models import Count
from django.shortcuts import render

from projeto.forms import ProjetoComponenteForm
from projeto.models import ProjetoComponente, Projeto
from projeto.views.login import LoggedInMixin


def ProjetoComponenteAjax(request, pk):
    projetocomponentes = ProjetoComponente.objects.filter(projeto_id=int(pk)).order_by('numero')

    return render(request, 'projetocomponentes.html', {'projetocomponentes': projetocomponentes})


class ProjetoComponenteList(LoggedInMixin, ListView):
    allowed_sort_fields = {'nome': {'default_direction': '', 'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 10

    template_name = 'projetocomponente/crud/list.html'
    context_object_name = 'projetoscomponentes'
    model = ProjetoComponente
    fields = '__all__'

    success_url = reverse_lazy('list_projetocomponente_projeto')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(projeto_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProjetoComponenteList, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        context['projeto_id'] = 0

        if self.kwargs:
            context['projeto_id'] = self.kwargs['pk']

        return context


class ProjetoComponenteDetail(LoggedInMixin, DetailView):
    template_name = 'projetocomponente/crud/detail.html'
    context_object_name = 'projetocomponente'
    model = ProjetoComponente
    fields = '__all__'

    success_url = reverse_lazy('list_projetocomponente_projeto')


class ProjetoComponenteCreate(LoggedInMixin, CreateView):
    template_name = 'projetocomponente/crud/form.html'
    form_class = ProjetoComponenteForm

    success_url = reverse_lazy('new_projetocomponente_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ProjetoComponenteCreate, self).form_valid(form)

    def get_initial(self):
        try:
            return {'criado_por': self.request.user.id, 'numero': int(ProjetoComponente.objects.latest('data_atualizado').numero) + 1}
        except ProjetoComponente.DoesNotExist:
            return {'criado_por': self.request.user.id}

    def get_context_data(self, **kwargs):
        context = super(ProjetoComponenteCreate,
                        self).get_context_data(**kwargs)

        if self.request.user.is_superuser:
            context["projetos"] = ProjetoComponente.objects.values('projeto_id').annotate(total=Count('projeto_id')).order_by('projeto_id')
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))
            context["projetos"] = ProjetoComponente.objects.filter(projeto__in=projetos.all()).values('projeto_id').annotate(total=Count('projeto_id')).order_by('projeto_id')

        return context

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(ProjetoComponenteCreate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class ProjetoComponenteUpdate(LoggedInMixin, UpdateView):
    template_name = 'projetocomponente/crud/form.html'
    form_class = ProjetoComponenteForm
    model = ProjetoComponente

    success_url = reverse_lazy('new_projetocomponente_projeto')

    def get_context_data(self, **kwargs):
        context = super(ProjetoComponenteUpdate,
                        self).get_context_data(**kwargs)
        context["projetocomponentes"] = ProjetoComponente.objects.all()
        return context

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(ProjetoComponenteUpdate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class ProjetoComponenteDelete(LoggedInMixin, DeleteView):
    template_name = 'projetocomponente/crud/delete.html'
    model = ProjetoComponente
    success_url = reverse_lazy('list_projetocomponente_projeto')
