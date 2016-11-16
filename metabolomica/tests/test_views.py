from django.test import TestCase
from django.urls import reverse


#
# Metabolomica's Views Tests
#

# Sample Tests
class MetabolomicaSampleHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_sample'), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaSampleNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_sample'), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaSampleListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_sample'), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaSampleDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_sample', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaSampleUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_sample', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaSampleDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_sample', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Experiment Tests
class MetabolomicaExperimentHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_experiment'), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaExperimentNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_experiment'), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaExperimentListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_experiment'), follow=True)
        self.assertEqual(response.status_code, 200)


# Equipment Tests
class MetabolomicaEquipmentHomeTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_equipment'), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaEquipmentNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_equipment'), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaEquipmentListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_equipment'), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaEquipmentDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_equipment', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaEquipmentUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_equipment', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaEquipmentDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_equipment', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


# Result Tests
class MetabolomicaHomeResultTest(TestCase):

    def test_home_http_response_code(self):
        response = self.client.get(reverse('home_result'), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaResultNewTest(TestCase):

    def test_new_http_response_code(self):
        response = self.client.get(reverse('new_result'), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaResultListTest(TestCase):

    def test_list_http_response_code(self):
        response = self.client.get(reverse('list_result'), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaResultDetailTest(TestCase):

    def test_detail_http_response_code(self):
        response = self.client.get(reverse('detail_result', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaResultUpdateTest(TestCase):

    def test_update_http_response_code(self):
        response = self.client.get(reverse('update_result', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)


class MetabolomicaResultDeleteTest(TestCase):

    def test_delete_http_response_code(self):
        response = self.client.get(reverse('delete_result', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)
