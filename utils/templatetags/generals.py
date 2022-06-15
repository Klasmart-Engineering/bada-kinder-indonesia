import requests

from django.conf import settings
from django import template


register = template.Library()


@register.simple_tag
def levels():
    r = requests.get(
        f'{settings.CMS_BASE_URL}/api/levels?sort[0]=ordering',
        headers={'Authorization': f'bearer {settings.STRAPI_API_KEY}'}
    )
    data = r.json()['data']
    return data
