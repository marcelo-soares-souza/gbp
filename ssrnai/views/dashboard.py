from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView

from projeto.views.login import LoggedInMixin
from ssrnai.models import Database

import logging
logger = logging.getLogger('ssrnai')

class DashboardSsrnaiDetail(LoggedInMixin, DetailView):
    template_name = 'dashboard/dashboard-ssrnai-detail.html'
    context_object_name = 'database'
    model = Database
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(DashboardSsrnaiDetail, self).get_context_data(**kwargs)

        return context


class DashboardSsrnai(LoggedInMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardSsrnai, self).get_context_data(**kwargs)
        context['databases'] = Database.objects.all()

        return context