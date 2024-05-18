from django import template

register = template.Library()

@register.filter
def starts_with_dash(line):
    return line.startswith('-')

@register.filter
def get_project_url(value, delimeter="//"):
    return value.split(delimeter)[-1]