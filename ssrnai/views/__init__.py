# __init__.py
# flake8: noqa

from ssrnai.views.database import DatabaseList, DatabaseDetail, DatabaseCreate, DatabaseUpdate, DatabaseDelete
from ssrnai.views.dashboard import DashboardSsrnai
from ssrnai.views.databaseSerach import DatabaseSearch
from ssrnai.views.showOrganism import ShowOrganism
from ssrnai.views.percevejo.percevejo_database_serach import PercevejoDatabaseSearch
from ssrnai.views.buva.buva_database_serach import BuvaDatabaseSearch
from ssrnai.views.capim.capim_database_serach import CapimDatabaseSearch
from ssrnai.views.lagarta.lagarta_database_serach import LagartaDatabaseSearch
from ssrnai.views.nematoide.nematoide_database_serach import NematoideDatabaseSearch

__all__ = ['DatabaseList', 'DatabaseDetail', 'DatabaseCreate', 'DatabaseUpdate', 'DatabaseDelete', 'DashboardSsrnai', 'DatabaseSearch', 'ShowOrganism',
'BuvaDatabaseSearch', 'CapimDatabaseSearch', 'LagartaDatabaseSearch', 'NematoideDatabaseSearch', 'PercevejoDatabaseSearch']
