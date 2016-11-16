from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from metabolomica.forms import ResultForm
from metabolomica.models import Result
from projeto.views.login import LoggedInMixin


class ResultList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {
                'name':
                {'default_direction': '', 'verbose_name': 'Name'},
                'data_atualizado':
                {'default_direction': '', 'verbose_name': 'Modified'}
                           }  # Atualizado Em Modified

    default_sort_field = 'name'
    paginate_by = 5

    template_name = 'result/crud/list.html'
    context_object_name = 'results'
    model = Result
    fields = '__all__'

    success_url = reverse_lazy('list_result')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(
                                 metabolomica_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ResultList, self).get_context_data(**kwargs)
        context['metabolomicas'] = Result.objects.all()
        context['metabolomica_id'] = 0

        if self.kwargs:
            context['metabolomica_id'] = self.kwargs['pk']

        return context


class ResultDetail(LoggedInMixin, DetailView):
    template_name = 'result/crud/detail.html'
    context_object_name = 'result'
    model = Result
    fields = '__all__'

    success_url = reverse_lazy('list_result')


class ResultCreate(LoggedInMixin, CreateView):
    template_name = 'result/crud/form.html'
    form_class = ResultForm
    success_url = reverse_lazy('list_result')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ResultCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class ResultUpdate(LoggedInMixin, UpdateView):
    template_name = 'result/crud/form.html'
    form_class = ResultForm
    model = Result

    def get_context_data(self, **kwargs):
        context = super(ResultUpdate, self).get_context_data(**kwargs)
        context["results"] = Result.objects.all().order_by('numero')
        return context

    success_url = reverse_lazy('list_result')


class ResultDelete(LoggedInMixin, DeleteView):
    template_name = 'result/crud/delete.html'
    model = Result
    success_url = reverse_lazy('list_result')
