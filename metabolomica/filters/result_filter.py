from django.contrib.auth.models import User

import django_filters

from metabolomica.models import Result


class ResultFilter(django_filters.FilterSet):

    user = django_filters.CharFilter(lookup_expr='icontains')
    database = django_filters.CharFilter(lookup_expr='icontains')
    experiment = django_filters.CharFilter(lookup_expr='icontains')
    sample = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Result
        fields = {
        'user',
        'database',
        'experiment',
        }
