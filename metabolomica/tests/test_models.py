from django.test import TestCase

from metabolomica.models import Sample, Approach, Equipment, Result, Species, Formula, Analytical


#
# Metabolomica Model's Tests
#

class SampleModelTest(TestCase):

    def test_sample_lab_code(self):
        sample = Sample(lab_code="Sample")
        self.assertEqual(str(sample), sample.lab_code)

    def test_sample_verbose_name_plural(self):
        self.assertEqual(str(Sample._meta.verbose_name_plural), "samples")


class ApproachModelTest(TestCase):

    def test_approach_name(self):
        approach = Approach(name="Approach")
        self.assertEqual(str(approach), approach.name)

    def test_approach_verbose_name_plural(self):
        self.assertEqual(str(Approach._meta.verbose_name_plural), "approaches")


class EquipmentModelTest(TestCase):

    def test_equipment_name(self):
        equipment = Equipment(name="Equipment")
        self.assertEqual(str(equipment), equipment.name)

    def test_equipment_verbose_name_plural(self):
        self.assertEqual(str(Equipment._meta.verbose_name_plural), "equipments")


class ResultModelTest(TestCase):

    def test_result_name(self):
        result = Result(name="Result")
        self.assertEqual(str(result), result.name)

    def test_result_verbose_name_plural(self):
        self.assertEqual(str(Result._meta.verbose_name_plural), "results")


class SpeciesModelTest(TestCase):

    def test_species_name(self):
        species = Species(name="Species")
        self.assertEqual(str(species), species.scientific_name)

    def test_species_verbose_name_plural(self):
        self.assertEqual(str(Species._meta.verbose_name_plural), "species")


class FormulaModelTest(TestCase):

    def test_formula_common_name(self):
        formula = Formula(common_name="Formula")
        self.assertEqual(str(formula), formula.common_name)

    def test_formula_verbose_name_plural(self):
        self.assertEqual(str(Formula._meta.verbose_name_plural), "formulae")


class AnalyticalModeltTest(TestCase):

    def test_analytical_name(self):
        analytical = Analytical(name="Analytical")
        self.assertEqual(str(analytical), analytical.name)

    def test_analytical_verbose_name_plural(self):
        self.assertEqual(str(Analytical._meta.verbose_name_plural), "analytical methods")
