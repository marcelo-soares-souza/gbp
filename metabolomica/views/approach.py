from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from metabolomica.forms import ApproachForm
from metabolomica.models import Approach
from projeto.views.login import LoggedInMixin


class ApproachList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {
                  'name':
                  {'default_direction': '', 'verbose_name': 'Name'},
                  'data_atualizado':
                  {'default_direction': '', 'verbose_name': 'Modified'}
                           }  # Atualizado Em Modified

    default_sort_field = 'name'
    paginate_by = 5

    template_name = 'approach/crud/list.html'
    context_object_name = 'approaches'
    model = Approach
    fields = '__all__'

    success_url = reverse_lazy('list_approach')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(
                                   metabolomica_id=int(self.kwargs['pk'])
                                                          )
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ApproachList, self).get_context_data(**kwargs)
        context['metabolomicas'] = Approach.objects.all()
        context['metabolomica_id'] = 0

        if self.kwargs:
            context['metabolomica_id'] = self.kwargs['pk']

        return context


class ApproachDetail(LoggedInMixin, DetailView):
    template_name = 'approach/crud/detail.html'
    context_object_name = 'approach'
    model = Approach
    fields = '__all__'

    success_url = reverse_lazy('list_approach')


class ApproachCreate(LoggedInMixin, CreateView):
    template_name = 'approach/crud/form.html'
    form_class = ApproachForm
    success_url = reverse_lazy('list_approach')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ApproachCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class ApproachUpdate(LoggedInMixin, UpdateView):
    template_name = 'approach/crud/form.html'
    form_class = ApproachForm
    model = Approach

    def get_context_data(self, **kwargs):
        context = super(ApproachUpdate, self).get_context_data(**kwargs)
        context["approaches"] = Approach.objects.all().order_by('data_atualizado')
        return context

    success_url = reverse_lazy('list_approach')


class ApproachDelete(LoggedInMixin, DeleteView):
    template_name = 'approach/crud/delete.html'
    model = Approach
    success_url = reverse_lazy('list_approach')
