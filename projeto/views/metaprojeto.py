from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.db.models import Q
from django.db.models import Count
from django.shortcuts import render

from projeto.forms import MetaProjetoForm
from projeto.models import MetaProjeto, Projeto
from projeto.views.login import LoggedInMixin


def MetaProjetoAjax(request, pk):
    metaprojetos = MetaProjeto.objects.filter(projeto_id=int(pk)).order_by('numero')

    return render(request, 'metaprojetos.html', {'metaprojetos': metaprojetos})


class MetaProjetoList(LoggedInMixin, ListView):
    allowed_sort_fields = {'nome': {'default_direction': '',
                                    'verbose_name': 'Nome'},
                           'data_atualizado': {'default_direction': '',
                                               'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'nome'
    paginate_by = 10

    template_name = 'metaprojeto/crud/list.html'
    context_object_name = 'metaprojeto'
    model = MetaProjeto
    fields = '__all__'

    success_url = reverse_lazy('list_metaprojeto_projeto')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(projeto_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(MetaProjetoList, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        context['projeto_id'] = 0

        if self.kwargs:
            context['projeto_id'] = self.kwargs['pk']

        return context


class MetaProjetoDetail(LoggedInMixin, DetailView):
    template_name = 'metaprojeto/crud/detail.html'
    context_object_name = 'metaprojeto'
    model = MetaProjeto
    fields = '__all__'

    success_url = reverse_lazy('list_metaprojeto_projeto')


class MetaProjetoCreate(LoggedInMixin, CreateView):
    template_name = 'metaprojeto/crud/form.html'
    form_class = MetaProjetoForm

    success_url = reverse_lazy('new_metaprojeto_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(MetaProjetoCreate, self).form_valid(form)

    def get_initial(self):
        try:
            return {'criado_por': self.request.user.id, 'numero': int(MetaProjeto.objects.latest('data_atualizado').numero) + 1}
        except MetaProjeto.DoesNotExist:
            return {'criado_por': self.request.user.id}

    def get_context_data(self, **kwargs):
        context = super(MetaProjetoCreate, self).get_context_data(**kwargs)
        context["projetos"] = MetaProjeto.objects.values('projeto_id').annotate(total=Count('projeto_id')).order_by('projeto_id')

        return context

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(MetaProjetoCreate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class MetaProjetoUpdate(LoggedInMixin, UpdateView):
    template_name = 'metaprojeto/crud/form.html'
    form_class = MetaProjetoForm
    model = MetaProjeto

    success_url = reverse_lazy('list_metaprojeto_projeto')

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(MetaProjetoUpdate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class MetaProjetoDelete(LoggedInMixin, DeleteView):
    template_name = 'metaprojeto/crud/delete.html'
    model = MetaProjeto
    success_url = reverse_lazy('list_metaprojeto_projeto')
