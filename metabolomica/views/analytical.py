import collections

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from metabolomica.forms import AnalyticalForm
from metabolomica.models import Analytical
from projeto.views.login import LoggedInMixin


class AnalyticalList(LoggedInMixin, SortableListView):
    allowed_sort_fields = collections.OrderedDict()
    allowed_sort_fields['name'] = {'default_direction': '', 'verbose_name': 'Name'}
    allowed_sort_fields['data_atualizado'] = {'default_direction': '', 'verbose_name': 'Updated'}

    default_sort_field = 'name'
    paginate_by = 10

    template_name = 'analytical/crud/list.html'
    context_object_name = 'analyticals'
    model = Analytical
    fields = '__all__'

    success_url = reverse_lazy('list_analytical')


class AnalyticalDetail(LoggedInMixin, DetailView):
    template_name = 'analytical/crud/detail.html'
    context_object_name = 'analytical'
    model = Analytical
    fields = '__all__'

    success_url = reverse_lazy('list_analytical')


class AnalyticalCreate(LoggedInMixin, CreateView):
    template_name = 'analytical/crud/form.html'
    form_class = AnalyticalForm
    success_url = reverse_lazy('list_analytical')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(AnalyticalCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class AnalyticalUpdate(LoggedInMixin, UpdateView):
    template_name = 'analytical/crud/form.html'
    form_class = AnalyticalForm
    model = Analytical

    def get_context_data(self, **kwargs):
        context = super(AnalyticalUpdate, self).get_context_data(**kwargs)
        context["analyticals"] = Analytical.objects.all().order_by('data_atualizado')
        return context

    success_url = reverse_lazy('list_analytical')


class AnalyticalDelete(LoggedInMixin, DeleteView):
    template_name = 'analytical/crud/delete.html'
    model = Analytical

    success_url = reverse_lazy('list_analytical')
