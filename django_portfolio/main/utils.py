from django import template

register = template.Library()


@register.filter
def starts_with_dash(value):
    return value.startswith("-")
