from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from sortable_listview import SortableListView

from projeto.views.login import LoggedInMixin
from projeto.models import Resultado
from projeto.forms import ResultadoForm

'''

'''

class ResultadoProjetoList(LoggedInMixin, SortableListView):
    allowed_sort_fields = {'numero': {'default_direction': '', 'verbose_name': 'Numero'},
                           'data_atualizado': {'default_direction': '', 'verbose_name': 'Atualizado Em'}}

    default_sort_field = 'numero'
    paginate_by = 5

    template_name = 'resultado/crud/list.html'
    context_object_name = 'resultados'
    model = Resultado
    fields = '__all__'

    success_url = reverse_lazy('list_resultado_projeto')

class ResultadoProjetoDetail(LoggedInMixin, DetailView):
    template_name = 'resultado/crud/detail.html'
    context_object_name = 'resultado'
    model = Resultado
    fields = '__all__'

    success_url = reverse_lazy('list_resultado_projeto')

class ResultadoProjetoCreate(LoggedInMixin, CreateView):
    template_name = 'resultado/crud/form.html'
    form_class = ResultadoForm
    
    success_url = reverse_lazy('list_resultado_projeto')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ResultadoProjetoCreate, self).form_valid(form)

    def get_initial(self):
        return { 'criado_por': self.request.user.id }

class ResultadoProjetoUpdate(LoggedInMixin, UpdateView):
    template_name = 'resultado/crud/form.html'
    form_class = ResultadoForm
    model = Resultado

    success_url = reverse_lazy('list_resultado_projeto')

class ResultadoProjetoDelete(LoggedInMixin, DeleteView):
    template_name = 'resultado/crud/delete.html'
    model = Resultado
    success_url = reverse_lazy('list_resultado_projeto')
