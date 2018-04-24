# __init__.py

from projeto.views.home import Home, Permission, jBrowse, Timeline
from projeto.views.instituicao import InstituicaoProjetoList, InstituicaoProjetoDetail, InstituicaoProjetoCreate, InstituicaoProjetoUpdate, InstituicaoProjetoDelete
from projeto.views.projeto import ProjetoList, ProjetoDetail, ProjetoCreate, ProjetoUpdate, ProjetoDelete, ProjetoDashboard
from projeto.views.objetivo import ObjetivoProjetoList, ObjetivoProjetoDetail, ObjetivoProjetoCreate, ObjetivoProjetoUpdate, ObjetivoProjetoDelete
from projeto.views.resultado import ResultadoProjetoList, ResultadoProjetoDetail, ResultadoProjetoCreate, ResultadoProjetoUpdate, ResultadoProjetoDelete
from projeto.views.palavrachave import PalavraChaveList, PalavraChaveDetail, PalavraChaveCreate, PalavraChaveUpdate, PalavraChaveDelete
from projeto.views.metaprojeto import MetaProjetoList, MetaProjetoDetail, MetaProjetoCreate, MetaProjetoUpdate, MetaProjetoDelete
from projeto.views.projetocomponente import ProjetoComponenteList, ProjetoComponenteDetail, ProjetoComponenteCreate, ProjetoComponenteUpdate, ProjetoComponenteDelete
from projeto.views.planoacao import PlanoAcaoList, PlanoAcaoDetail, PlanoAcaoCreate, PlanoAcaoUpdate, PlanoAcaoDelete
from projeto.views.atividade import AtividadeList, AtividadeDetail, AtividadeCreate, AtividadeUpdate, AtividadeDelete
from projeto.views.tarefa import TarefaList, TarefaDetail, TarefaCreate, TarefaUpdate, TarefaDelete

__all__ = ['Home', 'Permission', 'jBrowse', 'Timeline',
           'InstituicaoProjetoList', 'InstituicaoProjetoDetail', 'InstituicaoProjetoCreate', 'InstituicaoProjetoUpdate', 'InstituicaoProjetoDelete',
           'ProjetoList', 'ProjetoDetail', 'ProjetoCreate', 'ProjetoUpdate', 'ProjetoDelete', 'ProjetoDashboard',
           'ObjetivoProjetoList', 'ObjetivoProjetoDetail', 'ObjetivoProjetoCreate', 'ObjetivoProjetoUpdate', 'ObjetivoProjetoDelete',
           'ResultadoProjetoList', 'ResultadoProjetoDetail', 'ResultadoProjetoCreate', 'ResultadoProjetoUpdate', 'ResultadoProjetoDelete',
           'PalavraChaveList', 'PalavraChaveDetail', 'PalavraChaveCreate', 'PalavraChaveUpdate', 'PalavraChaveDelete',
           'MetaProjetoList', 'MetaProjetoDetail', 'MetaProjetoCreate', 'MetaProjetoUpdate', 'MetaProjetoDelete',
           'ProjetoComponenteList', 'ProjetoComponenteDetail', 'ProjetoComponenteCreate', 'ProjetoComponenteUpdate', 'ProjetoComponenteDelete',
           'PlanoAcaoList', 'PlanoAcaoDetail', 'PlanoAcaoCreate', 'PlanoAcaoUpdate', 'PlanoAcaoDelete',
           'AtividadeList', 'AtividadeDetail', 'AtividadeCreate', 'AtividadeUpdate', 'AtividadeDelete',
           'TarefaList', 'TarefaDetail', 'TarefaCreate', 'TarefaUpdate', 'TarefaDelete'
           ]
