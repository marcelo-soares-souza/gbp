import collections

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from metabolomica.forms import MsModeForm
from metabolomica.models import MsMode
from projeto.views.login import LoggedInMixin


class MsModeList(LoggedInMixin, SortableListView):
    allowed_sort_fields = collections.OrderedDict()
    allowed_sort_fields['name'] = {'default_direction': '', 'verbose_name': 'Name'}
    allowed_sort_fields['data_atualizado'] = {'default_direction': '', 'verbose_name': 'Modified'}

    default_sort_field = 'name'
    paginate_by = 10

    template_name = 'ms_mode/crud/list.html'
    context_object_name = 'ms_modes'
    model = MsMode
    fields = '__all__'

    success_url = reverse_lazy('list_ms_mode')


class MsModeDetail(LoggedInMixin, DetailView):
    template_name = 'ms_mode/crud/detail.html'
    context_object_name = 'ms_mode'
    model = MsMode
    fields = '__all__'

    success_url = reverse_lazy('list_ms_mode')


class MsModeCreate(LoggedInMixin, CreateView):
    template_name = 'ms_mode/crud/form.html'
    form_class = MsModeForm
    success_url = reverse_lazy('list_ms_mode')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(MsModeCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class MsModeUpdate(LoggedInMixin, UpdateView):
    template_name = 'ms_mode/crud/form.html'
    form_class = MsModeForm
    model = MsMode

    def get_context_data(self, **kwargs):
        context = super(MsModeUpdate, self).get_context_data(**kwargs)
        context["ms_modes"] = MsMode.objects.all().order_by('data_atualizado')
        return context

    success_url = reverse_lazy('list_ms_mode')


class MsModeDelete(LoggedInMixin, DeleteView):
    template_name = 'ms_mode/crud/delete.html'
    model = MsMode

    success_url = reverse_lazy('list_ms_mode')
