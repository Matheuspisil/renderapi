from django import template
from datetime import date
register = template.Library()


@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})


@register.filter(name='add_error_class')
def add_error_class(field, css_class):
    if field.errors:
        return field.as_widget(attrs={'class': css_class})
    return field.as_widget()


@register.filter(name='format_date')
def format_date(value):
    if isinstance(value, date):
        return value.strftime("%d/%m/%Y")
    return value
