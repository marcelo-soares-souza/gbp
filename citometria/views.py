from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from citometria.forms import CitometriaForm
from citometria.models import Citometria
from projeto.views.login import LoggedInMixin


class CitometriaList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'organismo': {'default_direction': '', 'verbose_name': 'Organismo'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'organismo'
    citometriate_by = 5

    template_name = 'citometria/crud/list.html'
    context_object_name = 'citometria'
    model = Citometria
    fields = '__all__'

    success_url = reverse_lazy('list_citometria')


class CitometriaDetail(LoggedInMixin, DetailView):
    template_name = 'citometria/crud/detail.html'
    context_object_name = 'citometria'
    model = Citometria
    fields = '__all__'

    success_url = reverse_lazy('list_citometria')


class CitometriaCreate(LoggedInMixin, CreateView):
    template_name = 'citometria/crud/form.html'
    form_class = CitometriaForm

    success_url = reverse_lazy('list_citometria')

    def get_context_data(self, **kwargs):
        context = super(CitometriaCreate, self).get_context_data(**kwargs)
        context["citometria"] = Citometria.objects.all()
        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(CitometriaCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class CitometriaUpdate(LoggedInMixin, UpdateView):
    template_name = 'citometria/crud/form.html'
    form_class = CitometriaForm
    model = Citometria

    success_url = reverse_lazy('list_citometria')

    def get_context_data(self, **kwargs):
        context = super(CitometriaUpdate, self).get_context_data(**kwargs)
        context["citometria"] = Citometria.objects.all()
        return context


class CitometriaDelete(LoggedInMixin, DeleteView):
    template_name = 'citometria/crud/delete.html'
    model = Citometria
    success_url = reverse_lazy('list_citometria')
