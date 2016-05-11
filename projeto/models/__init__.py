# __init__.py

from projeto.models.template import TemplateModelMixin
from projeto.models.instituicao import Instituicao
from projeto.models.projeto import Projeto
from projeto.models.objetivo import Objetivo
from projeto.models.resultado import Resultado
from projeto.models.palavrachave import PalavraChave
from projeto.models.metaprojeto import MetaProjeto
from projeto.models.projetocomponente import ProjetoComponente
from projeto.models.planoacao import PlanoAcao
from projeto.models.atividade import Atividade
from projeto.models.tarefa import Tarefa

__all__ = ['TemplateModelMixin',
           'instituicao', 'projeto', 'objetivo',
           'resultado', 'palavrachave', 'metaprojeto',
           'projetocomponente', 'planoacao', 'atividade', 'tarefa']
