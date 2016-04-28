from platform import python_version
from django import get_version


def django_version(request):
    return {'django_version': get_version() + ' with Python ' + python_version()}
