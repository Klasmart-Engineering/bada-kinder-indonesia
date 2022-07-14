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

@register.simple_tag
def name_initials(value):
    """ 
    Returns the first character of firstname and lastname in lowercase for a given name
    """
    names = value.split()
    first_name_initial = names[0][0]
    last_name_initial = ""
    if len(names) > 1:
        last_name_initial = names[-1][0]
    return f"{first_name_initial}{last_name_initial}"
