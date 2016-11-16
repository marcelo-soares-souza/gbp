from django.test import TestCase

from projeto.models import Projeto


#
# Projeto's Model Tests
#

class TestProjetoModel(TestCase):

    def test_return_sigla(self):
        sigla = Projeto(sigla="sigla")
        self.assertEqual(str(sigla), sigla.sigla)

#    def test_return_status(self):
#        status = Projeto(status="status")
#        self.assertEqual(str(status), Projeto.STATUS[Projeto.status])

    def test_verbose_name_plural(self):
        self.assertEqual(Projeto._meta.verbose_name_plural, "projetos")
