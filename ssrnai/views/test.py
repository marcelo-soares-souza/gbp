from django.views.generic import TemplateView

from projeto.views.login import LoggedInMixin
from ssrnai.models import Database

import logging
logger = logging.getLogger('ssrnai')


class Test(LoggedInMixin, TemplateView):
    template_name = 'test/test.html'

    def get_context_data(self, **kwargs):
        context = super(Test, self).get_context_data(**kwargs)
        context['databases'] = Database.objects.all()

        return context