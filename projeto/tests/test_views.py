from django.test import TestCase
from django.urls import reverse


#
# Projeto's View Tests
#

# Projeto Tests
class ProjetoNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Instituicao Tests
class ProjetoInstuicaoHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_instituicao_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoInstituicaoNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_instituicao_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoInstituicaoListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_instituicao_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoInstituicaoDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_instituicao_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoInstituicaoUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_instituicao_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoInstituicaoDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_instituicao_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Objetivo Tests
class ProjetoObjetivoHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_objetivo_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoObjetivoNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_objetivo_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoObjetivoListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_objetivo_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoObjetivoDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_objetivo_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoObjetivoUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_objetivo_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoObjetivoDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_objetivo_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Resultado Tests
class ProjetoResultadoHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_resultado_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoResultadoNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_resultado_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoResultadoListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_resultado_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoResultadoDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_resultado_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoResultadoUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_resultado_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoResultadoDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_resultado_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Projeto Componente Tests
class ProjetoComponenteHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_projetocomponente_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoComponenteNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_projetocomponente_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoComponenteListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_projetocomponente_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoComponenteDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_projetocomponente_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoComponenteUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_projetocomponente_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoComponenteDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_projetocomponente_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Plano de Ação Tests
class PlanoAcaoHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_planoacao_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class PlanoAcaoNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_planoacao_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class PlanoAcaoListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_planoacao_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class PlanoAcaoDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_planoacao_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class PlanoAcaoUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_planoacao_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class PlanoAcaoDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_planoacao_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Tarefa Tests
class ProjetoTarefaHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_tarefa_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoTarefaNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_tarefa_projeto'), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoTarefaListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_tarefa_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoDetailListTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_tarefa_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoTarefaUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_tarefa_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ProjetoTarefaDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_tarefa_projeto', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Tipo de Sequenciamento
class TipoSequenciamentoHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_tiposequenciamento'), follow=True)
        self.assertEqual(response.status_code, 200)


class TipoSequenciamentoNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_tiposequenciamento'), follow=True)
        self.assertEqual(response.status_code, 200)


class TipoSequenciamentoListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_tiposequenciamento'), follow=True)
        self.assertEqual(response.status_code, 200)


class TipoSequenciamentoDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_tiposequenciamento', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class TipoSequenciamentoUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_tiposequenciamento', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class TipoSequenciamentoDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_tiposequenciamento', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Contrato Tests
class ContratoHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_contrato'), follow=True)
        self.assertEqual(response.status_code, 200)


class ContratoNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_contrato', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ContratoListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_contrato', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ContratoDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_contrato', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ContratoUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_contrato', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class ContratoDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_contrato', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Dashboard Sequenciamento Tests
class DashboardSequenciamentoTest(TestCase):

    def test_dashboard(self):
        response = self.client.get(reverse('dashboard_sequenciamento', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Páginas Tests
class PaginaHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_pagina'), follow=True)
        self.assertEqual(response.status_code, 200)


class PaginaNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_pagina'), follow=True)
        self.assertEqual(response.status_code, 200)


class PaginaListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_pagina'), follow=True)
        self.assertEqual(response.status_code, 200)


class PaginaDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_pagina', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class PaginaUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_pagina', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class PaginaDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_pagina', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)
