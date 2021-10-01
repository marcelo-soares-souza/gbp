from ssrnai.models import Organisms
from django.views.generic import DetailView
from projeto.views.login import LoggedInMixin

import logging
logger = logging.getLogger('ssrnai')


class Result(LoggedInMixin, DetailView):
    template_name = 'result/result.html'
    context_object_name = 'database'
    model = Organisms
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(Result, self).get_context_data(**kwargs)
        context['organisms'] = Organisms.objects.filter(id=int(self.kwargs['pk']))

        query = self.request.GET.get('q')

        if query:
            context['results'] = context['results'].filter(organism_name__icontains=query)

            context['results'] = context['results'].distinct()

        context