import collections

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from metabolomica.forms import EquipmentForm
from metabolomica.models import Equipment
from projeto.views.login import LoggedInMixin


class EquipmentList(LoggedInMixin, SortableListView):
    allowed_sort_fields = collections.OrderedDict()
    allowed_sort_fields['name'] = {'default_direction': '', 'verbose_name': 'System'}
    allowed_sort_fields['data_atualizado'] = {'default_direction': '', 'verbose_name': 'Updated'}

    default_sort_field = 'name'
    paginate_by = 10

    template_name = 'equipment/crud/list.html'
    context_object_name = 'equipments'
    model = Equipment
    fields = '__all__'

    success_url = reverse_lazy('list_equipment')


class EquipmentDetail(LoggedInMixin, DetailView):
    template_name = 'equipment/crud/detail.html'
    context_object_name = 'equipment'
    model = Equipment
    fields = '__all__'

    success_url = reverse_lazy('list_equipment')


class EquipmentCreate(LoggedInMixin, CreateView):
    template_name = 'equipment/crud/form.html'
    form_class = EquipmentForm
    success_url = reverse_lazy('list_equipment')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(EquipmentCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class EquipmentUpdate(LoggedInMixin, UpdateView):
    template_name = 'equipment/crud/form.html'
    form_class = EquipmentForm
    model = Equipment

    def get_context_data(self, **kwargs):
        context = super(EquipmentUpdate, self).get_context_data(**kwargs)
        context["equipments"] = Equipment.objects.all().order_by('data_atualizado')
        return context

    success_url = reverse_lazy('list_equipment')


class EquipmentDelete(LoggedInMixin, DeleteView):
    template_name = 'equipment/crud/delete.html'
    model = Equipment

    success_url = reverse_lazy('list_equipment')
