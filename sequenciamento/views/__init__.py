# __init__.py

from django.shortcuts import render

from sequenciamento.views.tiposequenciamento import TipoSequenciamentoList, TipoSequenciamentoDetail, TipoSequenciamentoCreate, TipoSequenciamentoUpdate, TipoSequenciamentoDelete
from sequenciamento.views.sequenciamento import SequenciamentoList, SequenciamentoDetail, SequenciamentoCreate, SequenciamentoUpdate, SequenciamentoDelete

__all__ = ['TipoSequenciamentoList', 'TipoSequenciamentoDetail', 'TipoSequenciamentoCreate', 'TipoSequenciamentoUpdate', 'TipoSequenciamentoDelete', 'SequenciamentoList', 'SequenciamentoDetail', 'SequenciamentoCreate', 'SequenciamentoUpdate', 'SequenciamentoDelete']
