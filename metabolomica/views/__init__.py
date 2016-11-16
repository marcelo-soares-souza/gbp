# __init__.py
# flake8: noqa

from metabolomica.views.sample import SampleList, SampleDetail, SampleCreate, SampleUpdate, SampleDelete
from metabolomica.views.experiment import ExperimentList, ExperimentDetail, ExperimentCreate, ExperimentUpdate, ExperimentDelete
from metabolomica.views.equipment import EquipmentList, EquipmentDetail, EquipmentCreate, EquipmentUpdate, EquipmentDelete
from metabolomica.views.result import ResultList, ResultDetail, ResultCreate, ResultUpdate, ResultDelete


__all__ = [
           'SampleList', 'SampleDetail', 'SampleCreate', 'SampleUpdate', 'SampleDelete',
           'ExperimentList', 'ExperimentDetail', 'ExperimentCreate', 'ExperimentUpdate', 'ExperimentDelete',
           'EquipmentList', 'EquipmentDetail', 'EquipmentCreate', 'EquipmentUpdate', 'EquipmentDelete',
           'ResultList', 'ResultDetail', 'ResultCreate', 'ResultUpdate', 'ResultDelete',
           ]
