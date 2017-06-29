import collections

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from sortable_listview import SortableListView

from metabolomica.forms import DatabaseForm
from metabolomica.models import Database
from projeto.views.login import LoggedInMixin


class DatabaseList(LoggedInMixin, SortableListView):
    allowed_sort_fields = collections.OrderedDict()
    allowed_sort_fields['name'] = {'default_direction': '', 'verbose_name': 'Name'}
    allowed_sort_fields['data_atualizado'] = {'default_direction': '', 'verbose_name': 'Modified'}

    default_sort_field = 'name'
    paginate_by = 10

    template_name = 'database/crud/list.html'
    context_object_name = 'databases'
    model = Database
    fields = '__all__'

    success_url = reverse_lazy('list_database')


class DatabaseDetail(LoggedInMixin, DetailView):
    template_name = 'database/crud/detail.html'
    context_object_name = 'database'
    model = Database
    fields = '__all__'

    success_url = reverse_lazy('list_database')


class DatabaseCreate(LoggedInMixin, CreateView):
    template_name = 'database/crud/form.html'
    form_class = DatabaseForm
    success_url = reverse_lazy('list_database')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(DatabaseCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class DatabaseUpdate(LoggedInMixin, UpdateView):
    template_name = 'database/crud/form.html'
    form_class = DatabaseForm
    model = Database

    def get_context_data(self, **kwargs):
        context = super(DatabaseUpdate, self).get_context_data(**kwargs)
        context["databases"] = Database.objects.all().order_by('data_atualizado')
        return context

    success_url = reverse_lazy('list_database')


class DatabaseDelete(LoggedInMixin, DeleteView):
    template_name = 'database/crud/delete.html'
    model = Database

    success_url = reverse_lazy('list_database')
