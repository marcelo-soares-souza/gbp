# __init__.py
# flake8: noqa

from ssrnai.views.database import DatabaseList, DatabaseDetail, DatabaseCreate, DatabaseUpdate, DatabaseDelete
from ssrnai.views.dashboard import DashboardSsrnai
from ssrnai.views.databaseSerach import DatabaseSearch
from ssrnai.views.showOrganism import ShowOrganism

__all__ = ['DatabaseList', 'DatabaseDetail', 'DatabaseCreate', 'DatabaseUpdate', 'DatabaseDelete', 'DashboardSsrnai', 'DatabaseSearch', 'ShowOrganism',]
