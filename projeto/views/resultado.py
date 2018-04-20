from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.db.models import Q

from django.db.models import Count
from django.shortcuts import render

from projeto.forms import ResultadoForm
from projeto.models import Resultado, Projeto
from projeto.views.login import LoggedInMixin


def ResultadosAjax(request, pk):
    resultados = Resultado.objects.filter(projeto_id=int(pk)).order_by('numero')

    return render(request, 'resultados.html', {'resultados': resultados})


class ResultadoProjetoList(LoggedInMixin, ListView):
    allowed_sort_fields = {'numero': {'default_direction': '', 'verbose_name': 'Numero'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'numero'
    paginate_by = 10

    template_name = 'resultado/crud/list.html'
    context_object_name = 'resultados'
    model = Resultado
    fields = '__all__'

    success_url = reverse_lazy('list_resultado_projeto')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(projeto_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ResultadoProjetoList, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        context['projeto_id'] = 0

        if self.kwargs:
            context['projeto_id'] = self.kwargs['pk']

        return context


class ResultadoProjetoDetail(LoggedInMixin, DetailView):
    template_name = 'resultado/crud/detail.html'
    context_object_name = 'resultado'
    model = Resultado
    fields = '__all__'

    success_url = reverse_lazy('list_resultado_projeto')


class ResultadoProjetoCreate(LoggedInMixin, CreateView):
    template_name = 'resultado/crud/form.html'
    form_class = ResultadoForm

    success_url = reverse_lazy('new_resultado_projeto')

    def get_context_data(self, **kwargs):
        context = super(ResultadoProjetoCreate,
                        self).get_context_data(**kwargs)

        context["projetos"] = Resultado.objects.values('projeto_id').annotate(total=Count('projeto_id')).order_by('projeto_id')

        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ResultadoProjetoCreate, self).form_valid(form)

    def get_initial(self):
        try:
            return {'criado_por': self.request.user.id, 'numero': int(Resultado.objects.latest('data_atualizado').numero) + 1}
        except Resultado.DoesNotExist:
            return {'criado_por': self.request.user.id}

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(ResultadoProjetoCreate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class ResultadoProjetoUpdate(LoggedInMixin, UpdateView):
    template_name = 'resultado/crud/form.html'
    form_class = ResultadoForm
    model = Resultado

    success_url = reverse_lazy('list_resultado_projeto')

    def get_context_data(self, **kwargs):
        context = super(ResultadoProjetoUpdate,
                        self).get_context_data(**kwargs)
        context["resultados"] = Resultado.objects.all().order_by('numero')
        return context

    def get_form_kwargs(self):
        if self.request.user.is_superuser:
            projetos = Projeto.objects.all()
        else:
            projetos = Projeto.objects.filter(Q(colaborador__in=[self.request.user.id]) | Q(criado_por=self.request.user.id) | Q(lider=self.request.user.id))

        kwargs = super(ResultadoProjetoUpdate, self).get_form_kwargs()
        kwargs.update({'projetos': projetos})

        return kwargs


class ResultadoProjetoDelete(LoggedInMixin, DeleteView):
    template_name = 'resultado/crud/delete.html'
    model = Resultado
    success_url = reverse_lazy('list_resultado_projeto')
