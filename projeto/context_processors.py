from platform import python_version
from django import get_version

from sequenciamento.models.sequenciamento import Sequenciamento
from sequenciamento.models.tiposequenciamento import TipoSequenciamento
from sequenciamento.models.tarefasequenciamento import TarefaSequenciamento

def django_version(request):
    return {'django_version': get_version() + ' with Python ' + python_version()}

def stats(request):
    return {'count_sequenciamento': '(' + str(Sequenciamento.objects.count()) + ')',
            'count_tiposequenciamento': '(' + str(TipoSequenciamento.objects.count()) + ')',
            'count_tarefasequenciamento': '(' + str(TarefaSequenciamento.objects.count()) + ')'}
