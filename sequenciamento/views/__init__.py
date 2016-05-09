# __init__.py

from sequenciamento.views.tiposequenciamento import TipoSequenciamentoList, TipoSequenciamentoDetail, TipoSequenciamentoCreate, TipoSequenciamentoUpdate, TipoSequenciamentoDelete
from sequenciamento.views.sequenciamento import SequenciamentoList, SequenciamentoDetail, SequenciamentoCreate, SequenciamentoUpdate, SequenciamentoDelete
from sequenciamento.views.tarefasequenciamento import TarefaSequenciamentoList, TarefaSequenciamentoDetail, TarefaSequenciamentoCreate, TarefaSequenciamentoUpdate, TarefaSequenciamentoDelete

__all__ = ['TipoSequenciamentoList', 'TipoSequenciamentoDetail', 'TipoSequenciamentoCreate', 'TipoSequenciamentoUpdate',
           'TipoSequenciamentoDelete', 'SequenciamentoList', 'SequenciamentoDetail', 'SequenciamentoCreate', 'SequenciamentoUpdate', 'SequenciamentoDelete',
           'TarefaSequenciamentoList', 'TarefaSequenciamentoDetail', 'TarefaSequenciamentoCreate', 'TarefaSequenciamentoUpdate', 'TarefaSequenciamentoDelete']
