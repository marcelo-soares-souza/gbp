from django.test import TestCase

from metabolomica.models import Sample, Approach, Equipment, Result


#
# Metabolomica Model's Tests
#

class SampleModelTest(TestCase):

    def test_name(self):
        sample = Sample(lab_code="Sample")
        self.assertEqual(str(sample), sample.lab_code)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Sample._meta.verbose_name_plural), "samples")


class ApproachModelTest(TestCase):

    def test_name(self):
        approach = Approach(name="Approach")
        self.assertEqual(str(approach), approach.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Approach._meta.verbose_name_plural), "approaches")


class EquipmentModelTest(TestCase):

    def test_name(self):
        equipment = Equipment(name="Equipment")
        self.assertEqual(str(equipment), equipment.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Equipment._meta.verbose_name_plural), "equipments")


class ResultModelTest(TestCase):

    def test_name(self):
        result = Result(name="Result")
        self.assertEqual(str(result), result.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Result._meta.verbose_name_plural), "results")
