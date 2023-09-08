from django import template

register = template.Library()


# Создание тега
@register.filter()
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '#'


@register.simple_tag()
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '#'


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
