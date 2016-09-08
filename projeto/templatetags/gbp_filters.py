from django import template
from django.contrib.auth.models import Group


register = template.Library()


@register.filter(name='verifyfullname')
def verifyfullname(value):
    if value.first_name:
        return '%s %s' % (value.first_name, value.last_name)
    else:
        return value


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False
