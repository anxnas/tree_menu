from django import template
from tree_menu.models import Menu, MenuItem
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.inclusion_tag('tree_menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    try:
        menu = Menu.objects.get(name=menu_name)
        items = MenuItem.objects.filter(menu=menu).select_related('parent')
        return {'menu': menu, 'items': items, 'request': request}
    except ObjectDoesNotExist:
        return {'menu': None, 'items': [], 'request': request}