from django.conf import settings
from django import template

from utils import models

from bada_kinder_website.views import get_pacakage_id

register = template.Library()


@register.simple_tag
def user_package_id(request):
    pacakage_id = get_pacakage_id(request)
    return pacakage_id


@register.simple_tag
def settings():
    return models.SiteSettings.load()
