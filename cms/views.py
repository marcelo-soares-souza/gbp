from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from cms.forms import PaginaForm
from cms.models import Pagina
from projeto.views.login import LoggedInMixin


class PaginaList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'titulo': {'default_direction': '', 'verbose_name': 'Titulo'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'titulo'
    paginate_by = 5

    template_name = 'pagina/crud/list.html'
    context_object_name = 'pagina'
    model = Pagina
    fields = '__all__'

    success_url = reverse_lazy('list_pagina')


class PaginaDetail(LoggedInMixin, DetailView):
    template_name = 'pagina/crud/detail.html'
    context_object_name = 'pagina'
    model = Pagina
    fields = '__all__'

    success_url = reverse_lazy('list_pagina')


class PaginaCreate(LoggedInMixin, CreateView):
    template_name = 'pagina/crud/form.html'
    form_class = PaginaForm

    success_url = reverse_lazy('list_pagina')

    def get_context_data(self, **kwargs):
        context = super(PaginaCreate, self).get_context_data(**kwargs)
        context["pagina"] = Pagina.objects.all()
        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(PaginaCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class PaginaUpdate(LoggedInMixin, UpdateView):
    template_name = 'pagina/crud/form.html'
    form_class = PaginaForm
    model = Pagina

    # success_url = reverse_lazy('detail_pagina')

    def get_success_url(self):
        return reverse_lazy('detail_pagina', kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        context = super(PaginaUpdate, self).get_context_data(**kwargs)
        context["pagina"] = Pagina.objects.all()
        return context


class PaginaDelete(LoggedInMixin, DeleteView):
    template_name = 'pagina/crud/delete.html'
    model = Pagina
    success_url = reverse_lazy('list_pagina')


class PaginaContent(DetailView):
    template_name = 'pagina/crud/content.html'
    context_object_name = 'pagina'
    model = Pagina
    fields = '__all__'
