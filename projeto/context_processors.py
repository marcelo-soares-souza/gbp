from platform import python_version

from django import get_version
from django.db.models import Q

from projeto.models.atividade import Atividade
from projeto.models.instituicao import Instituicao
from projeto.models.metaprojeto import MetaProjeto
from projeto.models.objetivo import Objetivo
from projeto.models.palavrachave import PalavraChave
from projeto.models.planoacao import PlanoAcao
from projeto.models.projeto import Projeto
from projeto.models.projetocomponente import ProjetoComponente
from projeto.models.resultado import Resultado
from projeto.models.tarefa import Tarefa
from sequenciamento.models.sequenciamento import Sequenciamento
from sequenciamento.models.tarefasequenciamento import TarefaSequenciamento
from sequenciamento.models.tiposequenciamento import TipoSequenciamento
from sequenciamento.models.contrato import Contrato


def django_version(request):
    return {'django_version': get_version() + ' with Python ' + python_version()}


def stats(request):
    return {'count_contrato': '(' + str(Contrato.objects.count()) + ')',
            'count_sequenciamento': '(' + str(Sequenciamento.objects.count()) + ')',
            'count_tiposequenciamento': '(' + str(TipoSequenciamento.objects.count()) + ')',
            'count_tarefasequenciamento': '(' + str(TarefaSequenciamento.objects.count()) + ')',
            'count_instituicao': '(' + str(Instituicao.objects.count()) + ')',
            'count_projeto': '(' + str(Projeto.objects.count()) + ')',
            'count_objetivo': '(' + str(Objetivo.objects.count()) + ')',
            'count_resultado': '(' + str(Resultado.objects.count()) + ')',
            'count_palavrachave': '(' + str(PalavraChave.objects.count()) + ')',
            'count_metaprojeto': '(' + str(MetaProjeto.objects.count()) + ')',
            'count_projetocomponente': '(' + str(ProjetoComponente.objects.count()) + ')',
            'count_planoacao': '(' + str(PlanoAcao.objects.count()) + ')',
            'count_atividade': '(' + str(Atividade.objects.count()) + ')',
            'count_tarefa': '(' + str(Tarefa.objects.count()) + ')'}


def all_projetos(request):
    if request.user.is_superuser:
        all_projetos = Projeto.objects.all()
    else:
        all_projetos = Projeto.objects.filter(Q(colaborador__in=[request.user.id]) | Q(criado_por=request.user.id) | Q(lider=request.user.id))

    return {'all_projetos': all_projetos}
