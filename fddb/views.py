from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView
from django.shortcuts import render

from fddb.forms import FddbForm
from fddb.models import Fddb
from projeto.views.login import LoggedInMixin


def FDDBAjax(request, acesso, folha):
    fddbs = Fddb.objects.filter(organismo=acesso, folha=folha)

    return render(request, 'fddb.html', {'fddbs': fddbs})


class FddbDashBoard(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'organismo': {'default_direction': '', 'verbose_name': 'Organismo'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'organismo'
    paginate_by = 5

    template_name = 'fddb/crud/dashboard.html'
    context_object_name = 'fddb'
    model = Fddb
    fields = '__all__'

    success_url = reverse_lazy('list_fddb')


class FddbList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'organismo': {'default_direction': '', 'verbose_name': 'Organismo'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'organismo'
    paginate_by = 5

    template_name = 'fddb/crud/list.html'
    context_object_name = 'fddb'
    model = Fddb
    fields = '__all__'

    success_url = reverse_lazy('list_fddb')


class FddbDetail(LoggedInMixin, DetailView):
    template_name = 'fddb/crud/detail.html'
    context_object_name = 'fddb'
    model = Fddb
    fields = '__all__'

    success_url = reverse_lazy('list_fddb')


class FddbCreate(LoggedInMixin, CreateView):
    template_name = 'fddb/crud/form.html'
    form_class = FddbForm

    success_url = reverse_lazy('list_fddb')

    def get_context_data(self, **kwargs):
        context = super(FddbCreate, self).get_context_data(**kwargs)
        context["fddb"] = Fddb.objects.all()
        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(FddbCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class FddbUpdate(LoggedInMixin, UpdateView):
    template_name = 'fddb/crud/form.html'
    form_class = FddbForm
    model = Fddb

    success_url = reverse_lazy('list_fddb')

    def get_context_data(self, **kwargs):
        context = super(FddbUpdate, self).get_context_data(**kwargs)
        context["fddb"] = Fddb.objects.all()
        return context


class FddbDelete(LoggedInMixin, DeleteView):
    template_name = 'fddb/crud/delete.html'
    model = Fddb
    success_url = reverse_lazy('list_fddb')
