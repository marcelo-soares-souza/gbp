import collections

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from metabolomica.forms import FormulaForm
from metabolomica.models import Formula
from projeto.views.login import LoggedInMixin


class FormulaList(LoggedInMixin, SortableListView):
    allowed_sort_fields = collections.OrderedDict()
    allowed_sort_fields['common_name'] = {'default_direction': '', 'verbose_name': 'Common Name'}
    allowed_sort_fields['chemical_formula'] = {'default_direction': '', 'verbose_name': 'Chemical Formula'}

    default_sort_field = 'common_name'
    paginate_by = 10

    template_name = 'formula/crud/list.html'
    context_object_name = 'formula'
    model = Formula
    fields = '__all__'

    success_url = reverse_lazy('list_formula')


class FormulaDetail(LoggedInMixin, DetailView):
    template_name = 'formula/crud/detail.html'
    context_object_name = 'formula'
    model = Formula
    fields = '__all__'

    success_url = reverse_lazy('list_formula')


class FormulaCreate(LoggedInMixin, CreateView):
    template_name = 'formula/crud/form.html'
    form_class = FormulaForm
    success_url = reverse_lazy('list_formula')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(FormulaCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class FormulaUpdate(LoggedInMixin, UpdateView):
    template_name = 'formula/crud/form.html'
    form_class = FormulaForm
    model = Formula

    def get_context_data(self, **kwargs):
        context = super(FormulaUpdate, self).get_context_data(**kwargs)
        context["formulas"] = Formula.objects.all().order_by('data_atualizado')
        return context

    success_url = reverse_lazy('list_formula')


class FormulaDelete(LoggedInMixin, DeleteView):
    template_name = 'formula/crud/delete.html'
    model = Formula
    success_url = reverse_lazy('list_formula')
