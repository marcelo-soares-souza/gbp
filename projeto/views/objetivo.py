from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from projeto.models import Objetivo
from projeto.forms import ObjetivoForm

#
#
# Objetivo de Projeto
#
#

class ObjetivoProjetoList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'descricao': {'default_direction': '', 'verbose_name': 'Descrição'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'descricao'
    paginate_by = 5

    template_name = 'objetivo/crud/list.html'
    context_object_name = 'objetivos'
    model = Objetivo
    fields = '__all__'

    success_url = reverse_lazy('list_objetivo_projeto')

class ObjetivoProjetoDetail(LoggedInMixin, DetailView):
    template_name = 'objetivo/crud/detail.html'
    context_object_name = 'objetivo'
    model = Objetivo
    fields = '__all__'

    success_url = reverse_lazy('list_objetivo_projeto')

class ObjetivoProjetoCreate(LoggedInMixin, CreateView):
    template_name = 'objetivo/crud/form.html'
    form_class = ObjetivoForm
    success_url = reverse_lazy('new_objetivo_projeto')
    
    def get_context_data(self, **kwargs):
        context = super(ObjetivoProjetoCreate, self).get_context_data(**kwargs)
        context["objetivos"] = Objetivo.objects.all()
        return context
                
    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ObjetivoProjetoCreate, self).form_valid(form)

    def get_initial(self):
        return { 'criado_por': self.request.user.id }

class ObjetivoProjetoUpdate(LoggedInMixin, UpdateView):
    template_name = 'objetivo/crud/form.html'
    form_class = ObjetivoForm
    model = Objetivo

    success_url = reverse_lazy('list_objetivo_projeto')

class ObjetivoProjetoDelete(LoggedInMixin, DeleteView):
    template_name = 'objetivo/crud/delete.html'
    model = Objetivo
    success_url = reverse_lazy('list_objetivo_projeto')
