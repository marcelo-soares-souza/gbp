from django.test import TestCase
from django.urls import reverse


#
# FDDB View Tests
#

# FDDB
class FddbHomeTest(TestCase):

    def test_home(self):
        response = self.client.get(reverse('home_fddb'), follow=True)
        self.assertEqual(response.status_code, 200)


class FddbNewTest(TestCase):

    def test_new(self):
        response = self.client.get(reverse('new_fddb'), follow=True)
        self.assertEqual(response.status_code, 200)


class FddbListTest(TestCase):

    def test_list(self):
        response = self.client.get(reverse('list_fddb'), follow=True)
        self.assertEqual(response.status_code, 200)


class FddbDetailTest(TestCase):

    def test_detail(self):
        response = self.client.get(reverse('detail_fddb', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class FddbUpdateTest(TestCase):

    def test_update(self):
        response = self.client.get(reverse('update_fddb', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class FddbDeleteTest(TestCase):

    def test_delete(self):
        response = self.client.get(reverse('delete_fddb', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class FddbAcessoTest(TestCase):

    def test_acesso(self):
        response = self.client.get(reverse('fddb_ajax', kwargs={'acesso': 1, 'folha': -1}), follow=True)
        self.assertEqual(response.status_code, 200)
