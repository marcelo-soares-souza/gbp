from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from sequenciamento.forms import ContratoForm
from sequenciamento.models import Contrato


class ContratoList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'empresa_executora': {'default_direction': '', 'verbose_name': 'Empresa Executora'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'empresa_executora'
    paginate_by = 5

    template_name = 'contrato/crud/list.html'
    context_object_name = 'contratos'
    model = Contrato
    fields = '__all__'

    success_url = reverse_lazy('list_contrato')


class ContratoDetail(LoggedInMixin, DetailView):
    template_name = 'contrato/crud/detail.html'
    context_object_name = 'contrato'
    model = Contrato
    fields = '__all__'

    success_url = reverse_lazy('list_contrato')


class ContratoCreate(LoggedInMixin, CreateView):
    template_name = 'contrato/crud/form.html'
    form_class = ContratoForm

    success_url = reverse_lazy('list_contrato')

    def get_context_data(self, **kwargs):
        context = super(ContratoCreate,
                        self).get_context_data(**kwargs)

        context["contratos"] = Contrato.objects.all()
        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ContratoCreate, self).form_valid(form)

    def get_initial(self):
        data = {'criado_por': self.request.user.id}

        return data


class ContratoUpdate(LoggedInMixin, UpdateView):
    template_name = 'contrato/crud/form.html'
    form_class = ContratoForm
    model = Contrato

    success_url = reverse_lazy('list_contrato')


class ContratoDelete(LoggedInMixin, DeleteView):
    template_name = 'contrato/crud/delete.html'
    model = Contrato
    success_url = reverse_lazy('list_contrato')
