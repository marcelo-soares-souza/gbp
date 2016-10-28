from django.test import TestCase

from metabolomica.models import Sample, Experiment, Equipment, Result


#
# Metabolomica Model's Tests
#

class SampleModelTest(TestCase):

    def test_name(self):
        sample = Sample(name="Sample")
        self.assertEqual(str(sample), sample.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Sample._meta.verbose_name_plural), "samples")


class ExperimentModelTest(TestCase):

    def test_name(self):
        experiment = Experiment(name="Experiment")
        self.assertEqual(str(experiment), experiment.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Experiment._meta.verbose_name_plural), "experiments")


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
