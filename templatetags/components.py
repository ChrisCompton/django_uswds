# https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/

from django import template
from django.urls import path, include

register = template.Library()


"""
Alert component

{% alert "warning" "profile" %}
"""
@register.simple_tag(name='alert')
def alert(heading, message, *args, **kwargs):
    # warning = kwargs["warning"]
    # profile = kwargs["profile"]
    partial = include(f"partials/alert.html")
    return partial.render({"heading": heading, "message": message})
