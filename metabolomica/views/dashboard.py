from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView

from projeto.views.login import LoggedInMixin
from metabolomica.models import Experiment, Result, Sample, Database


class DashboardDetail(LoggedInMixin, DetailView):
    template_name = 'dashboard/crud/dashboard-detail.html'
    context_object_name = 'database'
    model = Database
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(DashboardDetail, self).get_context_data(**kwargs)
        context['samples'] = Sample.objects.filter(database_id=int(self.kwargs['pk']))
        context['results'] = Result.objects.select_related('sample').filter(sample__in = context['samples'])
        context['sample_id'] = 0

        return context


class DashboardMetabolomica(LoggedInMixin, TemplateView):
    template_name = 'dashboard/crud/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardMetabolomica, self).get_context_data(**kwargs)
        context['databases'] = Database.objects.all()

        return context


class DashboardExperimentList(LoggedInMixin, ListView):
    template_name = 'dashboard/crud/experiments.html'
    context_object_name = 'experiments'
    model = Experiment
    fields = '__all__'

    success_url = reverse_lazy('dashboard_experiment')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(DashboardExperimentList, self).get_context_data(**kwargs)
        context['experiments_list'] = Experiment.objects.all()
        context['experiment_id'] = 0

        if self.kwargs:
            context['experiment_id'] = self.kwargs['pk']

        return context


class DashboardResultList(LoggedInMixin, ListView):
    template_name = 'dashboard/crud/results.html'
    context_object_name = 'results'
    model = Result
    fields = '__all__'

    success_url = reverse_lazy('dashboard_result')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(DashboardResultList, self).get_context_data(**kwargs)
        context['results_list'] = Result.objects.all()
        context['samples_list'] = Sample.objects.all()
        context['sample_id'] = 0
        context['result_id'] = 0

        if self.kwargs:
            context['result_id'] = self.kwargs['pk']

        return context


class DashboardResultSampleList(LoggedInMixin, ListView):
    template_name = 'dashboard/crud/results.html'
    context_object_name = 'results'
    model = Result
    fields = '__all__'

    success_url = reverse_lazy('dashboard_result')

    def get_queryset(self):
        if self.kwargs:
            queryset = self.model._default_manager.filter(sample_id=int(self.kwargs['pk']))
        else:
            queryset = self.model._default_manager.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(DashboardResultSampleList, self).get_context_data(**kwargs)
        context['results_list'] = Result.objects.all()
        context['samples_list'] = Sample.objects.all()
        context['sample_id'] = 0
        context['result_id'] = 0

        if self.kwargs:
            context['sample_id'] = self.kwargs['pk']

        return context
