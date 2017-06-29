import collections

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from metabolomica.forms import SpeciesForm
from metabolomica.models import Species
from projeto.views.login import LoggedInMixin


class SpeciesList(LoggedInMixin, SortableListView):
    allowed_sort_fields = collections.OrderedDict()
    allowed_sort_fields['name'] = {'default_direction': '', 'verbose_name': 'Name'}
    allowed_sort_fields['scientific_name'] = {'default_direction': '', 'verbose_name': 'Scientific Name'}

    default_sort_field = 'name'
    paginate_by = 10

    template_name = 'species/crud/list.html'
    context_object_name = 'species'
    model = Species
    fields = '__all__'

    success_url = reverse_lazy('list_species')


class SpeciesDetail(LoggedInMixin, DetailView):
    template_name = 'species/crud/detail.html'
    context_object_name = 'species'
    model = Species
    fields = '__all__'

    success_url = reverse_lazy('list_species')


class SpeciesCreate(LoggedInMixin, CreateView):
    template_name = 'species/crud/form.html'
    form_class = SpeciesForm
    success_url = reverse_lazy('list_species')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(SpeciesCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class SpeciesUpdate(LoggedInMixin, UpdateView):
    template_name = 'species/crud/form.html'
    form_class = SpeciesForm
    model = Species

    def get_context_data(self, **kwargs):
        context = super(SpeciesUpdate, self).get_context_data(**kwargs)
        context["specieses"] = Species.objects.all().order_by('data_atualizado')
        return context

    success_url = reverse_lazy('list_species')


class SpeciesDelete(LoggedInMixin, DeleteView):
    template_name = 'species/crud/delete.html'
    model = Species

    success_url = reverse_lazy('list_species')
