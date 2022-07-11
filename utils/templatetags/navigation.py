from django import template

register = template.Library()


FIRST_PATHS = ['main', 'rpp', 'activity-book', 'course-book', 'story-book']

@register.simple_tag
def active(path, name):
    try:
        first_path = path.split("/")[1]
    except:
        first_path = ''

    if first_path == name:
        return 'active'
    return ''

@register.simple_tag
def collapsed(path, section):
    try:
        first_path = path.split("/")[1]
    except:
        first_path = ''

    open_section = ""
    if first_path in FIRST_PATHS:
        open_section = "bada-kinder"
    elif first_path in ['checkhomework']:
        open_section = "homework"
    elif first_path in ['tutorial-pdf', 'tutorial-video']:
        open_section = "tutorial"

    if open_section == section:
        return ''
    return 'collapsed'

@register.simple_tag
def show(path, section):
    try:
        first_path = path.split("/")[1]
    except:
        first_path = ''

    open_section = ""
    if first_path in FIRST_PATHS:
        open_section = "bada-kinder"
    elif first_path in ['checkhomework']:
        open_section = "homework"
    elif first_path in ['tutorial-pdf', 'tutorial-video']:
        open_section = "tutorial"

    if open_section == section:
        return 'show'
    return ''