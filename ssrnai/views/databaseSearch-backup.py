from ssrnai.models import Database, Organisms
from django.views.generic import DetailView
from projeto.views.login import LoggedInMixin

import logging
logger = logging.getLogger('ssrnai')


class DatabaseSearch(LoggedInMixin, DetailView):
    template_name = 'databaseSearch/database-search.html'
    context_object_name = 'database'
    model = Database
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(DatabaseSearch, self).get_context_data(**kwargs)
        context['organisms'] = Organisms.objects.filter(database_id=int(self.kwargs['pk']))

        query = self.request.GET.get('q')

        if query:
            context['results'] = context['results'].filter(organism_name__icontains=query)

            context['results'] = context['results'].distinct()

        return context
