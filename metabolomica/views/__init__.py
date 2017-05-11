# __init__.py
# flake8: noqa

from metabolomica.views.sample import SampleList, SampleDetail, SampleCreate, SampleUpdate, SampleDelete
from metabolomica.views.approach import ApproachList, ApproachDetail, ApproachCreate, ApproachUpdate, ApproachDelete
from metabolomica.views.equipment import EquipmentList, EquipmentDetail, EquipmentCreate, EquipmentUpdate, EquipmentDelete
from metabolomica.views.result import ResultList, ResultDetail, ResultCreate, ResultUpdate, ResultDelete
from metabolomica.views.database import DatabaseList, DatabaseDetail, DatabaseCreate, DatabaseUpdate, DatabaseDelete
from metabolomica.views.species import SpeciesList, SpeciesDetail, SpeciesCreate, SpeciesUpdate, SpeciesDelete
from metabolomica.views.formula import FormulaList, FormulaDetail, FormulaCreate, FormulaUpdate, FormulaDelete


__all__ = [
           'SampleList', 'SampleDetail', 'SampleCreate', 'SampleUpdate', 'SampleDelete',
           'ApproachList', 'ApproachDetail', 'ApproachCreate', 'ApproachUpdate', 'ApproachDelete',
           'EquipmentList', 'EquipmentDetail', 'EquipmentCreate', 'EquipmentUpdate', 'EquipmentDelete',
           'ResultList', 'ResultDetail', 'ResultCreate', 'ResultUpdate', 'ResultDelete',
           'DatabaseList', 'DatabaseDetail', 'DatabaseCreate', 'DatabaseUpdate', 'DatabaseDelete',
           'SpeciesList', 'SpeciesDetail', 'SpeciesCreate', 'SpeciesUpdate', 'SpeciesDelete',
           'FormulaList', 'FormulaDetail', 'FormulaCreate', 'FormulaUpdate', 'FormulaDelete',
           ]
