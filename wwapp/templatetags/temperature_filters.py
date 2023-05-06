from django import template

register = template.Library()

@register.filter
def tempConv(celsius):
    return round((celsius * 9/5) +32)
