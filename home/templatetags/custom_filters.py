from django import template

register = template.Library()

@register.filter
def enumerate_and_split(value):
    items = value.split(',')
    return [(i+1, item.strip()) for i, item in enumerate(items)]