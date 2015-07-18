from django import template

register = template.Library()

@register.assignment_tag
def flag():
    return True

@register.assignment_tag
def nosoy():
    return 'nosoy'

