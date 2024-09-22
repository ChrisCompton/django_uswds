# https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/

from django import template
from django.urls import path, include

register = template.Library()


@register.inclusion_tag("partials/alert.html")
def alert(heading, message, style='info', *args, **kwargs):
    """
    Renders an alert component.

    Parameters:
    heading (str): The heading of the alert.
    message (str): The message of the alert.
    style (str): The style of the alert (default is 'info').

    Returns:
    dict: A dictionary with keys 'heading', 'message', and 'style' to be used in the template.

    Usage:
    {% alert "heading" "message" "style" %}
    """
    # warning = kwargs["warning"]
    # profile = kwargs["profile"]
    return {"heading": heading, "message": message, "style": style}
