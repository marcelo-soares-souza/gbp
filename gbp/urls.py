from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from projeto.views.home import Home, Permission
from projeto.views.instituicao import InstituicaoProjetoList, InstituicaoProjetoDetail, InstituicaoProjetoCreate, InstituicaoProjetoUpdate, InstituicaoProjetoDelete
from projeto.views.projeto import ProjetoList, ProjetoDetail, ProjetoCreate, ProjetoUpdate, ProjetoDelete
from projeto.views.objetivo import ObjetivoProjetoList, ObjetivoProjetoDetail, ObjetivoProjetoCreate, ObjetivoProjetoUpdate, ObjetivoProjetoDelete
from projeto.views.resultado import ResultadoProjetoList, ResultadoProjetoDetail, ResultadoProjetoCreate, ResultadoProjetoUpdate, ResultadoProjetoDelete
from projeto.views.palavrachave import PalavraChaveList, PalavraChaveDetail, PalavraChaveCreate, PalavraChaveUpdate, PalavraChaveDelete
from projeto.views.metaprojeto import MetaProjetoList, MetaProjetoDetail, MetaProjetoCreate, MetaProjetoUpdate, MetaProjetoDelete
from projeto.views.projetocomponente import ProjetoComponenteList, ProjetoComponenteDetail, ProjetoComponenteCreate, ProjetoComponenteUpdate, ProjetoComponenteDelete
from projeto.views.planoacao import PlanoAcaoList, PlanoAcaoDetail, PlanoAcaoCreate, PlanoAcaoUpdate, PlanoAcaoDelete
from projeto.views.atividade import AtividadeList, AtividadeDetail, AtividadeCreate, AtividadeUpdate, AtividadeDelete
from projeto.views.tarefa import TarefaList, TarefaDetail, TarefaCreate, TarefaUpdate, TarefaDelete
from sequenciamento.views.tiposequenciamento import TipoSequenciamentoList, TipoSequenciamentoDetail, TipoSequenciamentoCreate, TipoSequenciamentoUpdate, TipoSequenciamentoDelete
from sequenciamento.views.sequenciamento import SequenciamentoList, SequenciamentoDetail, SequenciamentoCreate, SequenciamentoUpdate, SequenciamentoDelete
from sequenciamento.views.tarefasequenciamento import TarefaSequenciamentoList, TarefaSequenciamentoDetail, TarefaSequenciamentoCreate, TarefaSequenciamentoUpdate, TarefaSequenciamentoDelete

urlpatterns = [

    url(r'^$', Home.as_view(), name='home'),
    url(r'^permission/$', Permission.as_view(), name='permission_denied'),

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
    url(r'^objetivo/list/', ObjetivoProjetoList.as_view(),
        name='list_objetivo_projeto'),
    url(r'^objetivo/detail/(?P<pk>\d+)/$',
        ObjetivoProjetoDetail.as_view(), name='detail_objetivo_projeto'),
    url(r'^objetivo/update/(?P<pk>\d+)/$',
        ObjetivoProjetoUpdate.as_view(), name='update_objetivo_projeto'),
    url(r'^objetivo/delete/(?P<pk>\d+)/$',
        ObjetivoProjetoDelete.as_view(), name='delete_objetivo_projeto'),

    # Views de Resultado de Projeto
    url(r'^resultado/$', ResultadoProjetoList.as_view(),
        name='home_resultado_projeto'),
    url(r'^resultado/new/$', ResultadoProjetoCreate.as_view(),
        name='new_resultado_projeto'),
    url(r'^resultado/list/', ResultadoProjetoList.as_view(),
        name='list_resultado_projeto'),
    url(r'^resultado/detail/(?P<pk>\d+)/$',
        ResultadoProjetoDetail.as_view(), name='detail_resultado_projeto'),
    url(r'^resultado/update/(?P<pk>\d+)/$',
        ResultadoProjetoUpdate.as_view(), name='update_resultado_projeto'),
    url(r'^resultado/delete/(?P<pk>\d+)/$',
        ResultadoProjetoDelete.as_view(), name='delete_resultado_projeto'),


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
    url(r'^metaprojeto/list/', MetaProjetoList.as_view(),
        name='list_metaprojeto_projeto'),
    url(r'^metaprojeto/detail/(?P<pk>\d+)/$',
        MetaProjetoDetail.as_view(), name='detail_metaprojeto_projeto'),
    url(r'^metaprojeto/update/(?P<pk>\d+)/$',
        MetaProjetoUpdate.as_view(), name='update_metaprojeto_projeto'),
    url(r'^metaprojeto/delete/(?P<pk>\d+)/$',
        MetaProjetoDelete.as_view(), name='delete_metaprojeto_projeto'),

    # Views de Projeto Componente
    url(r'^projetocomponente/$', ProjetoComponenteList.as_view(),
        name='home_projetocomponente_projeto'),
    url(r'^projetocomponente/new/$', ProjetoComponenteCreate.as_view(),
        name='new_projetocomponente_projeto'),
    url(r'^projetocomponente/list/', ProjetoComponenteList.as_view(),
        name='list_projetocomponente_projeto'),
    url(r'^projetocomponente/detail/(?P<pk>\d+)/$',
        ProjetoComponenteDetail.as_view(), name='detail_projetocomponente_projeto'),
    url(r'^projetocomponente/update/(?P<pk>\d+)/$',
        ProjetoComponenteUpdate.as_view(), name='update_projetocomponente_projeto'),
    url(r'^projetocomponente/delete/(?P<pk>\d+)/$',
        ProjetoComponenteDelete.as_view(), name='delete_projetocomponente_projeto'),

    # Views de Plano de Ação
    url(r'^planoacao/$', PlanoAcaoList.as_view(), name='home_planoacao_projeto'),
    url(r'^planoacao/new/$', PlanoAcaoCreate.as_view(),
        name='new_planoacao_projeto'),
    url(r'^planoacao/list/', PlanoAcaoList.as_view(),
        name='list_planoacao_projeto'),
    url(r'^planoacao/detail/(?P<pk>\d+)/$',
        PlanoAcaoDetail.as_view(), name='detail_planoacao_projeto'),
    url(r'^planoacao/update/(?P<pk>\d+)/$',
        PlanoAcaoUpdate.as_view(), name='update_planoacao_projeto'),
    url(r'^planoacao/delete/(?P<pk>\d+)/$',
        PlanoAcaoDelete.as_view(), name='delete_planoacao_projeto'),

    # Views de Atividade
    url(r'^atividade/$', AtividadeList.as_view(), name='home_atividade_projeto'),
    url(r'^atividade/new/$', AtividadeCreate.as_view(),
        name='new_atividade_projeto'),
    url(r'^atividade/list/', AtividadeList.as_view(),
        name='list_atividade_projeto'),
    url(r'^atividade/detail/(?P<pk>\d+)/$',
        AtividadeDetail.as_view(), name='detail_atividade_projeto'),
    url(r'^atividade/update/(?P<pk>\d+)/$',
        AtividadeUpdate.as_view(), name='update_atividade_projeto'),
    url(r'^atividade/delete/(?P<pk>\d+)/$',
        AtividadeDelete.as_view(), name='delete_atividade_projeto'),

    # Views de Tarefa
    url(r'^tarefa/$', TarefaList.as_view(), name='home_tarefa_projeto'),
    url(r'^tarefa/new/$', TarefaCreate.as_view(), name='new_tarefa_projeto'),
    url(r'^tarefa/list/', TarefaList.as_view(), name='list_tarefa_projeto'),
    url(r'^tarefa/detail/(?P<pk>\d+)/$',
        TarefaDetail.as_view(), name='detail_tarefa_projeto'),
    url(r'^tarefa/update/(?P<pk>\d+)/$',
        TarefaUpdate.as_view(), name='update_tarefa_projeto'),
    url(r'^tarefa/delete/(?P<pk>\d+)/$',
        TarefaDelete.as_view(), name='delete_tarefa_projeto'),

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
    url(r'^tarefasequenciamento/list/', TarefaSequenciamentoList.as_view(),
        name='list_tarefasequenciamento'),
    url(r'^tarefasequenciamento/detail/(?P<pk>\d+)/$',
        TarefaSequenciamentoDetail.as_view(), name='detail_tarefasequenciamento'),
    url(r'^tarefasequenciamento/update/(?P<pk>\d+)/$',
        TarefaSequenciamentoUpdate.as_view(), name='update_tarefasequenciamento'),
    url(r'^tarefasequenciamento/delete/(?P<pk>\d+)/$',
        TarefaSequenciamentoDelete.as_view(), name='delete_tarefasequenciamento'),

    # Login e Logout
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # Interface Admin e Auth
    url(r'^admin/', include(admin.site.urls)),

    # Chained - Smart Select
    url(r'^chaining/', include('smart_selects.urls')),
]
