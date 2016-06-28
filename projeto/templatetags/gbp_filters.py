from django import template

register = template.Library()


@register.filter(name='verifyfullname')
def verifyfullname(value):
    if value.first_name:
        return '%s %s' % (value.first_name, value.last_name)
    else:
        return value
