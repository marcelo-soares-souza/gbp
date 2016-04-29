# __init__.py

from django.shortcuts import render

from sequenciamento.views.tiposequenciamento import TipoSequenciamentoList, TipoSequenciamentoDetail, TipoSequenciamentoCreate, TipoSequenciamentoUpdate, TipoSequenciamentoDelete

__all__ = ['TipoSequenciamentoList', 'TipoSequenciamentoDetail',
           'TipoSequenciamentoCreate', 'TipoSequenciamentoUpdate', 'TipoSequenciamentoDelete']
