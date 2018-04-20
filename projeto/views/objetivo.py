from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.db.models import Q

from django.db.models import Count
from django.shortcuts import render

from projeto.forms import ObjetivoForm
from projeto.models import Objetivo, Projeto
from projeto.views.login import LoggedInMixin


def ObjetivosAjax(request, pk):
    objetivos = Objetivo.objects.filter(projeto_id=int(pk)).order_by('numero')

    return render(request, 'objetivos.html', {'objetivos': objetivos})


class ObjetivoProjetoList(LoggedInMixin, ListView):
    allowed_sort_fields = {'descricao': {'default_direction': '', 'verbose_name': 'Descrição'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'descricao'
    paginate_by = 10

    template_name = 'objetivo/crud/list.html'
    context_object_name = 'objetivos'
    model = Objetivo
    fields = '__all__'

    success_url = reverse_lazy('list_objetivo_projeto')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(projeto_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ObjetivoProjetoList, self).get_context_data(**kwargs)

        if self.request.user.is_superuser:
            context['projetos'] = Projeto.objects.all()
            context['objetivos'] = Objetivo.objects.all()
        else:
            context['projetos'] = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))
            context['objetivos'] = Objetivo.objects.filter(projeto__in=context['projetos'].all().values_list('id'))

        context['projeto_id'] = 0

        if self.kwargs:
            context['projeto_id'] = self.kwargs['pk']

        return context


class ObjetivoProjetoDetail(LoggedInMixin, DetailView):
    template_name = 'objetivo/crud/detail.html'
    context_object_name = 'objetivo'
    model = Objetivo
    fields = '__all__'

    success_url = reverse_lazy('list_objetivo_projeto')


class ObjetivoProjetoCreate(LoggedInMixin, CreateView):
    template_name = 'objetivo/crud/form.html'
    form_class = ObjetivoForm
    success_url = reverse_lazy('new_objetivo_projeto')

    def get_context_data(self, **kwargs):
        context = super(ObjetivoProjetoCreate, self).get_context_data(**kwargs)

        if self.request.user.is_superuser:
            context["projetos"] = Objetivo.objects.values('projeto_id').annotate(total=Count('projeto_id')).order_by('projeto_id')
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))
            context["projetos"] = Objetivo.objects.filter(projeto__in=projetos.all()).values('projeto_id').annotate(total=Count('projeto_id')).order_by('projeto_id')

        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ObjetivoProjetoCreate, self).form_valid(form)

    def get_initial(self):
        try:
            return {'criado_por': self.request.user.id, 'numero': int(Objetivo.objects.latest('data_atualizado').numero) + 1}
        except Objetivo.DoesNotExist:
            return {'criado_por': self.request.user.id}

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(ObjetivoProjetoCreate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs

class ObjetivoProjetoUpdate(LoggedInMixin, UpdateView):
    template_name = 'objetivo/crud/form.html'
    form_class = ObjetivoForm
    model = Objetivo

    def get_context_data(self, **kwargs):
        context = super(ObjetivoProjetoUpdate, self).get_context_data(**kwargs)
        context["objetivos"] = Objetivo.objects.all().order_by('numero')
        return context

    success_url = reverse_lazy('new_objetivo_projeto')

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(ObjetivoProjetoUpdate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class ObjetivoProjetoDelete(LoggedInMixin, DeleteView):
    template_name = 'objetivo/crud/delete.html'
    model = Objetivo
    success_url = reverse_lazy('new_objetivo_projeto')
