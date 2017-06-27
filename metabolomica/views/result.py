import os
import collections
import csv

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from sortable_listview import SortableListView

from metabolomica.forms import ResultForm
from metabolomica.models import Result
from projeto.views.login import LoggedInMixin

import logging
logger = logging.getLogger('metabolomica')


class ResultList(LoggedInMixin, SortableListView):
    allowed_sort_fields = collections.OrderedDict()
    allowed_sort_fields['name'] = {'default_direction': '', 'verbose_name': 'Name'}
    allowed_sort_fields['data_atualizado'] = {'default_direction': '', 'verbose_name': 'Modified'}

    default_sort_field = 'name'
    paginate_by = 10

    template_name = 'result/crud/list.html'
    context_object_name = 'results'
    model = Result
    fields = '__all__'

    success_url = reverse_lazy('list_result')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(metabolomica_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ResultList, self).get_context_data(**kwargs)
        context['metabolomicas'] = Result.objects.all()
        context['metabolomica_id'] = 0

        if self.kwargs:
            context['metabolomica_id'] = self.kwargs['pk']

        return context


class ResultDetail(LoggedInMixin, DetailView):
    template_name = 'result/crud/detail.html'
    context_object_name = 'result'
    model = Result
    fields = '__all__'

    success_url = reverse_lazy('list_result')

    def get_context_data(self, **kwargs):
        context = super(ResultDetail, self).get_context_data(**kwargs)

        if context['result'].raw_data:
            reader = csv.DictReader(open(os.path.join(settings.BASE_DIR, 'media', str(context['result'].raw_data))), delimiter=';')
            result = []
            for line in reader:
                result.append(line)

            context['csv'] = result

        return context


class ResultCreate(LoggedInMixin, CreateView):
    template_name = 'result/crud/form.html'
    form_class = ResultForm
    success_url = reverse_lazy('list_result')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(ResultCreate, self).form_valid(form)

    def get_initial(self):
        return {'criado_por': self.request.user.id}


class ResultUpdate(LoggedInMixin, UpdateView):
    template_name = 'result/crud/form.html'
    form_class = ResultForm
    model = Result

    def get_context_data(self, **kwargs):
        context = super(ResultUpdate, self).get_context_data(**kwargs)
        context["results"] = Result.objects.all().order_by('data_atualizado')
        return context

    success_url = reverse_lazy('list_result')


class ResultDelete(LoggedInMixin, DeleteView):
    template_name = 'result/crud/delete.html'
    model = Result
    success_url = reverse_lazy('list_result')


class ResultFileUpload(LoggedInMixin, DetailView):
    def model_form_upload(request):
        if request.method == 'POST':
            form = ResultForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('result/crud/detail.html')
        else:
            form = ResultForm()
        return render(request, 'result/crud/detail.html', {
            'form': form
        })
