import collections

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from metabolomica.forms import SampleForm
from metabolomica.models import Sample
from projeto.views.login import LoggedInMixin


class SampleList(LoggedInMixin, SortableListView):
    allowed_sort_fields = collections.OrderedDict()
    allowed_sort_fields['lab_code'] = {'default_direction': '', 'verbose_name': 'Lab Code'}
    allowed_sort_fields['data_atualizado'] = {'default_direction': '', 'verbose_name': 'Modified'}

    default_sort_field = 'lab_code'
    paginate_by = 10

    template_name = 'sample/crud/list.html'
    context_object_name = 'samples'
    model = Sample
    fields = '__all__'

    success_url = reverse_lazy('list_sample')


class SampleDetail(LoggedInMixin, DetailView):
    template_name = 'sample/crud/detail.html'
    context_object_name = 'sample'
    model = Sample
    fields = '__all__'

    success_url = reverse_lazy('list_sample')


class SampleCreate(LoggedInMixin, CreateView):
    template_name = 'sample/crud/form.html'
    form_class = SampleForm

    success_url = reverse_lazy('list_sample')

    def get_context_data(self, **kwargs):
        context = super(SampleCreate, self).get_context_data(**kwargs)
        context["samples"] = Sample.objects.all()
        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(SampleCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class SampleUpdate(LoggedInMixin, UpdateView):
    template_name = 'sample/crud/form.html'
    form_class = SampleForm
    model = Sample

    success_url = reverse_lazy('list_sample')

    def get_context_data(self, **kwargs):
        context = super(SampleUpdate, self).get_context_data(**kwargs)
        context["samples"] = Sample.objects.all()
        return context


class SampleDelete(LoggedInMixin, DeleteView):
    template_name = 'sample/crud/delete.html'
    model = Sample
    success_url = reverse_lazy('list_sample')
