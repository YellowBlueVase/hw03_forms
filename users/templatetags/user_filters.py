from django import template

register = template.Library()


@register.filter
def addсlass(field, css):
    return field.as_widget(attrs={"class": css})
