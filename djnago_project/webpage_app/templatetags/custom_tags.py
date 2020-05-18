import datetime

from django import template


register = template.Library()



@register.simple_tag
def today():
    return datetime.datetime.today().time()

@register.simple_tag
def date():
    return  datetime.date.today()
