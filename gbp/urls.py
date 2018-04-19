from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

# URLs Projeto
from projeto.views.atividade import AtividadeCreate, AtividadeDelete, AtividadeDetail, AtividadeList, AtividadeUpdate
from projeto.views.home import Permission, jBrowse, Location, Timeline
from projeto.views.instituicao import InstituicaoProjetoCreate, InstituicaoProjetoDelete, InstituicaoProjetoDetail, InstituicaoProjetoList, InstituicaoProjetoUpdate
from projeto.views.metaprojeto import MetaProjetoCreate, MetaProjetoDelete, MetaProjetoDetail, MetaProjetoList, MetaProjetoUpdate
from projeto.views.objetivo import ObjetivoProjetoCreate, ObjetivoProjetoDelete, ObjetivoProjetoDetail, ObjetivoProjetoList, ObjetivoProjetoUpdate
from projeto.views.palavrachave import PalavraChaveCreate, PalavraChaveDelete, PalavraChaveDetail, PalavraChaveList, PalavraChaveUpdate
from projeto.views.planoacao import PlanoAcaoCreate, PlanoAcaoDelete, PlanoAcaoDetail, PlanoAcaoList, PlanoAcaoUpdate
from projeto.views.projeto import ProjetoCreate, ProjetoDelete, ProjetoDetail, ProjetoList, ProjetoUpdate
from projeto.views.projetocomponente import ProjetoComponenteCreate, ProjetoComponenteDelete, ProjetoComponenteDetail, ProjetoComponenteList, ProjetoComponenteUpdate
from projeto.views.resultado import ResultadoProjetoCreate, ResultadoProjetoDelete, ResultadoProjetoDetail, ResultadoProjetoList, ResultadoProjetoUpdate
from projeto.views.tarefa import TarefaCreate, TarefaDelete, TarefaDetail, TarefaList, TarefaUpdate
from projeto.views import objetivo, resultado, projetocomponente, metaprojeto, planoacao, atividade, tarefa

# URLs Sequenciamento
from sequenciamento.views.sequenciamento import SequenciamentoCreate, SequenciamentoDelete, SequenciamentoDetail, SequenciamentoList, SequenciamentoUpdate
from sequenciamento.views.tarefasequenciamento import TarefaSequenciamentoCreate, TarefaSequenciamentoDelete, TarefaSequenciamentoDetail, TarefaSequenciamentoList, TarefaSequenciamentoUpdate
from sequenciamento.views.tiposequenciamento import TipoSequenciamentoCreate, TipoSequenciamentoDelete, TipoSequenciamentoDetail, TipoSequenciamentoList, TipoSequenciamentoUpdate
from sequenciamento.views.contrato import ContratoCreate, ContratoDelete, ContratoDetail, ContratoList, ContratoUpdate
from sequenciamento.views.dashboard import DashboardList

# URLs CMS
from cms.views import PaginaCreate, PaginaDelete, PaginaDetail, PaginaList, PaginaUpdate, PaginaContent

# URLs FDDB
from fddb.views import FddbCreate, FddbDelete, FddbDetail, FddbList, FddbUpdate, FddbDashBoard, FDDBAjax

# URLs Metabolomica
from metabolomica.views.sample import SampleCreate, SampleDelete, SampleDetail, SampleList, SampleUpdate
from metabolomica.views.approach import ApproachCreate, ApproachDelete, ApproachDetail, ApproachList, ApproachUpdate
from metabolomica.views.equipment import EquipmentCreate, EquipmentDelete, EquipmentDetail, EquipmentList, EquipmentUpdate
from metabolomica.views.result import ResultCreate, ResultDelete, ResultDetail, ResultList, ResultUpdate
from metabolomica.views.database import DatabaseCreate, DatabaseDelete, DatabaseDetail, DatabaseList, DatabaseUpdate
from metabolomica.views.dashboard import DashboardMetabolomica, DashboardApproachList, DashboardResultList, DashboardResultSampleList, DashboardDetail
from metabolomica.views.species import SpeciesCreate, SpeciesDelete, SpeciesDetail, SpeciesList, SpeciesUpdate
from metabolomica.views.formula import FormulaCreate, FormulaDelete, FormulaDetail, FormulaList, FormulaUpdate
from metabolomica.views.analytical import AnalyticalCreate, AnalyticalDelete, AnalyticalDetail, AnalyticalList, AnalyticalUpdate

urlpatterns = [

    # url(r'^$', Home.as_view(), name='home'),
    url(r'^$', PaginaContent.as_view(), {'pk': 5}, name='home'),
    url(r'^permission/$', Permission.as_view(), name='permission_denied'),

    # General Info about LBB
    url(r'^jbrowse/$', jBrowse.as_view(), name='jbrowse'),
    url(r'^location/$', Location.as_view(), name='location'),
    url(r'^timeline/$', Timeline.as_view(), name='timeline'),

    # Views de Projeto
    url(r'^projeto/new/$', ProjetoCreate.as_view(), name='new_projeto'),
    url(r'^projeto/list/', ProjetoList.as_view(), name='list_projeto'),
    url(r'^projeto/detail/(?P<pk>\d+)/$', ProjetoDetail.as_view(), name='detail_projeto'),
    url(r'^projeto/update/(?P<pk>\d+)/$', ProjetoUpdate.as_view(), name='update_projeto'),
    url(r'^projeto/delete/(?P<pk>\d+)/$', ProjetoDelete.as_view(), name='delete_projeto'),

    # Views de Instituicao de Projeto
    url(r'^instituicao/$', InstituicaoProjetoList.as_view(),
        name='home_instituicao_projeto'),
    url(r'^instituicao/new/$', InstituicaoProjetoCreate.as_view(),
        name='new_instituicao_projeto'),
    url(r'^instituicao/list/', InstituicaoProjetoList.as_view(),
        name='list_instituicao_projeto'),
    url(r'^instituicao/detail/(?P<pk>\d+)/$',
        InstituicaoProjetoDetail.as_view(), name='detail_instituicao_projeto'),
    url(r'^instituicao/update/(?P<pk>\d+)/$',
        InstituicaoProjetoUpdate.as_view(), name='update_instituicao_projeto'),
    url(r'^instituicao/delete/(?P<pk>\d+)/$',
        InstituicaoProjetoDelete.as_view(), name='delete_instituicao_projeto'),

    # Views de Objetivo de Projeto
    url(r'^objetivo/$', ObjetivoProjetoList.as_view(),
        name='home_objetivo_projeto'),
    url(r'^objetivo/new/$', ObjetivoProjetoCreate.as_view(),
        name='new_objetivo_projeto'),
    url(r'^objetivo/list/projeto/(?P<pk>\d+)', ObjetivoProjetoList.as_view(),
        name='list_objetivo_projeto'),
    url(r'^objetivo/list/', ObjetivoProjetoList.as_view(),
        name='list_objetivo_projeto'),
    url(r'^objetivo/detail/(?P<pk>\d+)/$',
        ObjetivoProjetoDetail.as_view(), name='detail_objetivo_projeto'),
    url(r'^objetivo/update/(?P<pk>\d+)/$',
        ObjetivoProjetoUpdate.as_view(), name='update_objetivo_projeto'),
    url(r'^objetivo/delete/(?P<pk>\d+)/$',
        ObjetivoProjetoDelete.as_view(), name='delete_objetivo_projeto'),
    url(r'^objetivo/ajax/projeto/(?P<pk>\d+)$', objetivo.ObjetivosAjax, name='objetivos_ajax'),

    # Views de Resultado de Projeto
    url(r'^resultado/$', ResultadoProjetoList.as_view(),
        name='home_resultado_projeto'),
    url(r'^resultado/new/$', ResultadoProjetoCreate.as_view(),
        name='new_resultado_projeto'),
    url(r'^resultado/list/projeto/(?P<pk>\d+)', ResultadoProjetoList.as_view(),
        name='list_resultado_projeto'),
    url(r'^resultado/list/', ResultadoProjetoList.as_view(),
        name='list_resultado_projeto'),
    url(r'^resultado/detail/(?P<pk>\d+)/$',
        ResultadoProjetoDetail.as_view(), name='detail_resultado_projeto'),
    url(r'^resultado/update/(?P<pk>\d+)/$',
        ResultadoProjetoUpdate.as_view(), name='update_resultado_projeto'),
    url(r'^resultado/delete/(?P<pk>\d+)/$',
        ResultadoProjetoDelete.as_view(), name='delete_resultado_projeto'),
    url(r'^resultado/ajax/projeto/(?P<pk>\d+)$', resultado.ResultadosAjax, name='resultados_ajax'),

    # Views de Palavra Chave
    url(r'^palavrachave/$', PalavraChaveList.as_view(),
        name='home_palavrachave_projeto'),
    url(r'^palavrachave/new/$', PalavraChaveCreate.as_view(),
        name='new_palavrachave_projeto'),
    url(r'^palavrachave/list/', PalavraChaveList.as_view(),
        name='list_palavrachave_projeto'),
    url(r'^palavrachave/detail/(?P<pk>\d+)/$',
        PalavraChaveDetail.as_view(), name='detail_palavrachave_projeto'),
    url(r'^palavrachave/update/(?P<pk>\d+)/$',
        PalavraChaveUpdate.as_view(), name='update_palavrachave_projeto'),
    url(r'^palavrachave/delete/(?P<pk>\d+)/$',
        PalavraChaveDelete.as_view(), name='delete_palavrachave_projeto'),

    # Views de Metas de Projeto
    url(r'^metaprojeto/$', MetaProjetoList.as_view(),
        name='home_metaprojeto_projeto'),
    url(r'^metaprojeto/new/$', MetaProjetoCreate.as_view(),
        name='new_metaprojeto_projeto'),
    url(r'^metaprojeto/list/projeto/(?P<pk>\d+)', MetaProjetoList.as_view(),
        name='list_metaprojeto_projeto'),
    url(r'^metaprojeto/list/', MetaProjetoList.as_view(),
        name='list_metaprojeto_projeto'),
    url(r'^metaprojeto/detail/(?P<pk>\d+)/$',
        MetaProjetoDetail.as_view(), name='detail_metaprojeto_projeto'),
    url(r'^metaprojeto/update/(?P<pk>\d+)/$',
        MetaProjetoUpdate.as_view(), name='update_metaprojeto_projeto'),
    url(r'^metaprojeto/delete/(?P<pk>\d+)/$',
        MetaProjetoDelete.as_view(), name='delete_metaprojeto_projeto'),
    url(r'^metaprojeto/ajax/projeto/(?P<pk>\d+)$', metaprojeto.MetaProjetoAjax, name='metaprojetos_ajax'),

    # Views de Projeto Componente
    url(r'^projetocomponente/$', ProjetoComponenteList.as_view(),
        name='home_projetocomponente_projeto'),
    url(r'^projetocomponente/new/$', ProjetoComponenteCreate.as_view(),
        name='new_projetocomponente_projeto'),
    url(r'^projetocomponente/list/projeto/(?P<pk>\d+)', ProjetoComponenteList.as_view(),
        name='list_projetocomponente_projeto'),
    url(r'^projetocomponente/list/', ProjetoComponenteList.as_view(),
        name='list_projetocomponente_projeto'),
    url(r'^projetocomponente/detail/(?P<pk>\d+)/$',
        ProjetoComponenteDetail.as_view(), name='detail_projetocomponente_projeto'),
    url(r'^projetocomponente/update/(?P<pk>\d+)/$',
        ProjetoComponenteUpdate.as_view(), name='update_projetocomponente_projeto'),
    url(r'^projetocomponente/delete/(?P<pk>\d+)/$',
        ProjetoComponenteDelete.as_view(), name='delete_projetocomponente_projeto'),
    url(r'^projetocomponente/ajax/projeto/(?P<pk>\d+)$', projetocomponente.ProjetoComponenteAjax, name='projetocomponentes_ajax'),

    # Views de Plano de Ação
    url(r'^planoacao/$', PlanoAcaoList.as_view(), name='home_planoacao_projeto'),
    url(r'^planoacao/new/$', PlanoAcaoCreate.as_view(),
        name='new_planoacao_projeto'),
    url(r'^planoacao/list/projeto/(?P<pk>\d+)', PlanoAcaoList.as_view(),
        name='list_planoacao_projeto'),
    url(r'^planoacao/list/', PlanoAcaoList.as_view(),
        name='list_planoacao_projeto'),
    url(r'^planoacao/detail/(?P<pk>\d+)/$',
        PlanoAcaoDetail.as_view(), name='detail_planoacao_projeto'),
    url(r'^planoacao/update/(?P<pk>\d+)/$',
        PlanoAcaoUpdate.as_view(), name='update_planoacao_projeto'),
    url(r'^planoacao/delete/(?P<pk>\d+)/$',
        PlanoAcaoDelete.as_view(), name='delete_planoacao_projeto'),
    url(r'^planoacao/ajax/projeto/(?P<pk>\d+)$', planoacao.PlanoAcaoAjax, name='planoacaos_ajax'),
    url(r'^planoacao/ajax/projeto_componente/(?P<pk>\d+)$', planoacao.PlanoAcaoProjetoComponenteAjax, name='planoacaos_projeto_componente_ajax'),

    # Views de Atividade
    url(r'^atividade/$', AtividadeList.as_view(), name='home_atividade_projeto'),
    url(r'^atividade/new/$', AtividadeCreate.as_view(),
        name='new_atividade_projeto'),
    url(r'^atividade/list/projeto/(?P<pk>\d+)', AtividadeList.as_view(),
        name='list_atividade_projeto'),
    url(r'^atividade/list/', AtividadeList.as_view(),
        name='list_atividade_projeto'),
    url(r'^atividade/detail/(?P<pk>\d+)/$',
        AtividadeDetail.as_view(), name='detail_atividade_projeto'),
    url(r'^atividade/update/(?P<pk>\d+)/$',
        AtividadeUpdate.as_view(), name='update_atividade_projeto'),
    url(r'^atividade/delete/(?P<pk>\d+)/$',
        AtividadeDelete.as_view(), name='delete_atividade_projeto'),
    url(r'^atividade/ajax/projeto/(?P<pk>\d+)$', atividade.AtividadeAjax, name='atividades_ajax'),
    url(r'^atividade/ajax/planoacao/(?P<pk>\d+)$', atividade.AtividadePlanoAcaoAjax, name='atividades_planoacao_ajax'),

    # Views de Tarefa
    url(r'^tarefa/$', TarefaList.as_view(), name='home_tarefa_projeto'),
    url(r'^tarefa/new/$', TarefaCreate.as_view(), name='new_tarefa_projeto'),
    url(r'^tarefa/list/projeto/(?P<pk>\d+)', TarefaList.as_view(), name='list_tarefa_projeto'),
    url(r'^tarefa/list/', TarefaList.as_view(), name='list_tarefa_projeto'),
    url(r'^tarefa/detail/(?P<pk>\d+)/$',
        TarefaDetail.as_view(), name='detail_tarefa_projeto'),
    url(r'^tarefa/update/(?P<pk>\d+)/$',
        TarefaUpdate.as_view(), name='update_tarefa_projeto'),
    url(r'^tarefa/delete/(?P<pk>\d+)/$',
        TarefaDelete.as_view(), name='delete_tarefa_projeto'),
    url(r'^tarefa/ajax/projeto/(?P<pk>\d+)$', tarefa.TarefaAjax, name='tarefas_ajax'),
    url(r'^tarefa/ajax/planoacao/(?P<pk>\d+)$', tarefa.TarefaPlanoAcaoAjax, name='tarefas_planoacao_ajax'),

    # Views de Tipo Sequenciamento
    url(r'^tiposequenciamento/$', TipoSequenciamentoList.as_view(),
        name='home_tiposequenciamento'),
    url(r'^tiposequenciamento/new/$', TipoSequenciamentoCreate.as_view(),
        name='new_tiposequenciamento'),
    url(r'^tiposequenciamento/list/', TipoSequenciamentoList.as_view(),
        name='list_tiposequenciamento'),
    url(r'^tiposequenciamento/detail/(?P<pk>\d+)/$',
        TipoSequenciamentoDetail.as_view(), name='detail_tiposequenciamento'),
    url(r'^tiposequenciamento/update/(?P<pk>\d+)/$',
        TipoSequenciamentoUpdate.as_view(), name='update_tiposequenciamento'),
    url(r'^tiposequenciamento/delete/(?P<pk>\d+)/$',
        TipoSequenciamentoDelete.as_view(), name='delete_tiposequenciamento'),

    # Views de Sequenciamento
    url(r'^sequenciamento/$', SequenciamentoList.as_view(),
        name='home_sequenciamento'),
    url(r'^sequenciamento/new/$', SequenciamentoCreate.as_view(),
        name='new_sequenciamento'),
    url(r'^sequenciamento/new/(?P<pk>\d+)/$', SequenciamentoCreate.as_view(),
        name='new_sequenciamento'),
    url(r'^sequenciamento/new/(?P<option>[\w\-]+)/(?P<pk>\d+)/$', SequenciamentoCreate.as_view(),
        name='new_sequenciamento'),
    url(r'^sequenciamento/list/tipo/(?P<pk>\d+)$', SequenciamentoList.as_view(),
        name='list_sequenciamento'),
    url(r'^sequenciamento/list/', SequenciamentoList.as_view(),
        name='list_sequenciamento'),
    url(r'^sequenciamento/detail/(?P<pk>\d+)/$',
        SequenciamentoDetail.as_view(), name='detail_sequenciamento'),
    url(r'^sequenciamento/update/(?P<pk>\d+)/$',
        SequenciamentoUpdate.as_view(), name='update_sequenciamento'),
    url(r'^sequenciamento/delete/(?P<pk>\d+)/$',
        SequenciamentoDelete.as_view(), name='delete_sequenciamento'),

    # Views de Tarefa Sequenciamento
    url(r'^tarefasequenciamento/$', TarefaSequenciamentoList.as_view(),
        name='home_tarefasequenciamento'),
    url(r'^tarefasequenciamento/new/$', TarefaSequenciamentoCreate.as_view(),
        name='new_tarefasequenciamento'),
    url(r'^tarefasequenciamento/new/(?P<pk>\d+)/$', TarefaSequenciamentoCreate.as_view(),
        name='new_tarefasequenciamento'),
    url(r'^tarefasequenciamento/list/sequenciamento/(?P<pk>\d+)', TarefaSequenciamentoList.as_view(),
        name='list_tarefasequenciamento'),
    url(r'^tarefasequenciamento/list/', TarefaSequenciamentoList.as_view(),
        name='list_tarefasequenciamento'),
    url(r'^tarefasequenciamento/detail/(?P<pk>\d+)/$',
        TarefaSequenciamentoDetail.as_view(), name='detail_tarefasequenciamento'),
    url(r'^tarefasequenciamento/update/(?P<pk>\d+)/$',
        TarefaSequenciamentoUpdate.as_view(), name='update_tarefasequenciamento'),
    url(r'^tarefasequenciamento/delete/(?P<pk>\d+)/$',
        TarefaSequenciamentoDelete.as_view(), name='delete_tarefasequenciamento'),

    # Views de Contrato
    url(r'^contrato/$', ContratoList.as_view(),
        name='home_contrato'),
    url(r'^contrato/new/$', ContratoCreate.as_view(),
        name='new_contrato'),
    url(r'^contrato/new/(?P<pk>\d+)/$', ContratoCreate.as_view(),
        name='new_contrato'),
    url(r'^contrato/list/tipo/(?P<pk>\d+)$', ContratoList.as_view(),
        name='list_contrato'),
    url(r'^contrato/list/', ContratoList.as_view(),
        name='list_contrato'),
    url(r'^contrato/detail/(?P<pk>\d+)/$',
        ContratoDetail.as_view(), name='detail_contrato'),
    url(r'^contrato/update/(?P<pk>\d+)/$',
        ContratoUpdate.as_view(), name='update_contrato'),
    url(r'^contrato/delete/(?P<pk>\d+)/$',
        ContratoDelete.as_view(), name='delete_contrato'),

    # View Dashboard Sequenciamento
    url(r'^sequenciamento/dashboard/(?P<pk>\d+)/$', DashboardList.as_view(), name='dashboard_sequenciamento'),
    url(r'^sequenciamento/dashboard/', DashboardList.as_view(), name='dashboard_sequenciamento'),

    # Views de Páginas
    url(r'^pagina/$', PaginaList.as_view(), name='home_pagina'),
    url(r'^pagina/new/$', PaginaCreate.as_view(), name='new_pagina'),
    url(r'^pagina/list/', PaginaList.as_view(), name='list_pagina'),
    url(r'^pagina/detail/(?P<pk>\d+)/$', PaginaDetail.as_view(), name='detail_pagina'),
    url(r'^pagina/update/(?P<pk>\d+)/$', PaginaUpdate.as_view(), name='update_pagina'),
    url(r'^pagina/delete/(?P<pk>\d+)/$', PaginaDelete.as_view(), name='delete_pagina'),

    url(r'^cms/(?P<pk>\d+)/$', PaginaContent.as_view(), name='content_pagina'),

    # Views de FDDB
    url(r'^fddb/$', FddbDashBoard.as_view(), name='home_fddb'),
    url(r'^fddb/new/$', FddbCreate.as_view(), name='new_fddb'),
    url(r'^fddb/list/', FddbList.as_view(), name='list_fddb'),
    url(r'^fddb/detail/(?P<pk>\d+)/$', FddbDetail.as_view(), name='detail_fddb'),
    url(r'^fddb/update/(?P<pk>\d+)/$', FddbUpdate.as_view(), name='update_fddb'),
    url(r'^fddb/delete/(?P<pk>\d+)/$', FddbDelete.as_view(), name='delete_fddb'),
    url(r'^fddb/ajax/(?P<acesso>[\w\-]+)/(?P<folha>[\w\-]+)/$', FDDBAjax, name='fddb_ajax'),

    # Views de Sample
    url(r'^metabolomica/sample$', SampleList.as_view(), name='home_sample'),
    url(r'^metabolomica/sample/new/$', SampleCreate.as_view(), name='new_sample'),
    url(r'^metabolomica/sample/list/', SampleList.as_view(), name='list_sample'),
    url(r'^metabolomica/sample/detail/(?P<pk>\d+)/$', SampleDetail.as_view(), name='detail_sample'),
    url(r'^metabolomica/sample/update/(?P<pk>\d+)/$', SampleUpdate.as_view(), name='update_sample'),
    url(r'^metabolomica/sample/delete/(?P<pk>\d+)/$', SampleDelete.as_view(), name='delete_sample'),

    # Views de Approach
    url(r'^metabolomica/approach$', ApproachList.as_view(), name='home_approach'),
    url(r'^metabolomica/approach/new/$', ApproachCreate.as_view(), name='new_approach'),
    url(r'^metabolomica/approach/list/', ApproachList.as_view(), name='list_approach'),
    url(r'^metabolomica/approach/detail/(?P<pk>\d+)/$', ApproachDetail.as_view(), name='detail_approach'),
    url(r'^metabolomica/approach/update/(?P<pk>\d+)/$', ApproachUpdate.as_view(), name='update_approach'),
    url(r'^metabolomica/approach/delete/(?P<pk>\d+)/$', ApproachDelete.as_view(), name='delete_approach'),

    # Views de Equipment
    url(r'^metabolomica/equipment$', EquipmentList.as_view(), name='home_equipment'),
    url(r'^metabolomica/equipment/new/$', EquipmentCreate.as_view(), name='new_equipment'),
    url(r'^metabolomica/equipment/list/', EquipmentList.as_view(), name='list_equipment'),
    url(r'^metabolomica/equipment/detail/(?P<pk>\d+)/$', EquipmentDetail.as_view(), name='detail_equipment'),
    url(r'^metabolomica/equipment/update/(?P<pk>\d+)/$', EquipmentUpdate.as_view(), name='update_equipment'),
    url(r'^metabolomica/equipment/delete/(?P<pk>\d+)/$', EquipmentDelete.as_view(), name='delete_equipment'),

    # Views de Result
    url(r'^metabolomica/result$', ResultList.as_view(), name='home_result'),
    url(r'^metabolomica/result/new/$', ResultCreate.as_view(), name='new_result'),
    url(r'^metabolomica/result/list/', ResultList.as_view(), name='list_result'),
    url(r'^metabolomica/result/detail/(?P<pk>\d+)/$', ResultDetail.as_view(), name='detail_result'),
    url(r'^metabolomica/result/update/(?P<pk>\d+)/$', ResultUpdate.as_view(), name='update_result'),
    url(r'^metabolomica/result/delete/(?P<pk>\d+)/$', ResultDelete.as_view(), name='delete_result'),

    # Views de Database
    url(r'^metabolomica/database$', DatabaseList.as_view(), name='home_database'),
    url(r'^metabolomica/database/new/$', DatabaseCreate.as_view(), name='new_database'),
    url(r'^metabolomica/database/list/', DatabaseList.as_view(), name='list_database'),
    url(r'^metabolomica/database/detail/(?P<pk>\d+)/$', DatabaseDetail.as_view(), name='detail_database'),
    url(r'^metabolomica/database/update/(?P<pk>\d+)/$', DatabaseUpdate.as_view(), name='update_database'),
    url(r'^metabolomica/database/delete/(?P<pk>\d+)/$', DatabaseDelete.as_view(), name='delete_database'),

    # Views de Species
    url(r'^metabolomica/species$', SpeciesList.as_view(), name='home_species'),
    url(r'^metabolomica/species/new/$', SpeciesCreate.as_view(), name='new_species'),
    url(r'^metabolomica/species/list/$', SpeciesList.as_view(), name='list_species'),
    url(r'^metabolomica/species/detail/(?P<pk>\d+)/$', SpeciesDetail.as_view(), name='detail_species'),
    url(r'^metabolomica/species/update/(?P<pk>\d+)/$', SpeciesUpdate.as_view(), name='update_species'),
    url(r'^metabolomica/species/delete/(?P<pk>\d+)/$', SpeciesDelete.as_view(), name='delete_species'),

    # Views de Formula
    url(r'^metabolomica/formula$', FormulaList.as_view(), name='home_formula'),
    url(r'^metabolomica/formula/new/$', FormulaCreate.as_view(), name='new_formula'),
    url(r'^metabolomica/formula/list/$', FormulaList.as_view(), name='list_formula'),
    url(r'^metabolomica/formula/detail/(?P<pk>\d+)/$', FormulaDetail.as_view(), name='detail_formula'),
    url(r'^metabolomica/formula/update/(?P<pk>\d+)/$', FormulaUpdate.as_view(), name='update_formula'),
    url(r'^metabolomica/formula/delete/(?P<pk>\d+)/$', FormulaDelete.as_view(), name='delete_formula'),

    # Views de Analytical
    url(r'^metabolomica/analytical$', AnalyticalList.as_view(), name='home_analytical'),
    url(r'^metabolomica/analytical/new/$', AnalyticalCreate.as_view(), name='new_analytical'),
    url(r'^metabolomica/analytical/list/$', AnalyticalList.as_view(), name='list_analytical'),
    url(r'^metabolomica/analytical/detail/(?P<pk>\d+)/$', AnalyticalDetail.as_view(), name='detail_analytical'),
    url(r'^metabolomica/analytical/update/(?P<pk>\d+)/$', AnalyticalUpdate.as_view(), name='update_analytical'),
    url(r'^metabolomica/analytical/delete/(?P<pk>\d+)/$', AnalyticalDelete.as_view(), name='delete_analytical'),

    # Views DashBoard Metabolomica
    url(r'^metabolomica/dashboard/', DashboardMetabolomica.as_view(), name='dashboard_metabolomica'),
    url(r'^metabolomica/dashboard-detail/(?P<pk>\d+)/$', DashboardDetail.as_view(), name='dashboard_detail'),
    url(r'^metabolomica/dashboard-approach/(?P<pk>\d+)/$', DashboardApproachList.as_view(), name='dashboard_approach'),
    url(r'^metabolomica/dashboard-approach/', DashboardList.as_view(), name='dashboard_approach'),
    url(r'^metabolomica/dashboard-result/sample/(?P<pk>\d+)/$', DashboardResultSampleList.as_view(), name='dashboard_result_sample'),
    url(r'^metabolomica/dashboard-result/(?P<pk>\d+)/$', DashboardResultList.as_view(), name='dashboard_result'),
    url(r'^metabolomica/dashboard-result/', DashboardResultList.as_view(), name='dashboard_result'),

    # Login e Logout
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # Interface Admin e Auth
    url(r'^admin/', admin.site.urls),

    # Chained - Smart Select
    url(r'^chaining/', include('smart_selects.urls')),

    # CkEditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    # Attachments
    url(r'^attachments/', include('attachments.urls', namespace='attachments')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

