# -*- coding: utf-8 -*-

from django.utils import timezone


def get_current_year():
    return timezone.now().year


def _get_trail(request):
    trail = []
    current_page = request.current_page
    while current_page:
        trail.insert(0, current_page)
        current_page = current_page.parent_page
    return trail


def get_breadcrumbs_list(request):
    trail = _get_trail(request)
    breadcrumbs_list = [{'menu_title': u'Home', 'url': '/'}]
    for breadcrumb in trail:
        breadcrumbs_list.append({
            'menu_title': breadcrumb.get_menu_title(),
            'url': breadcrumb.get_absolute_url()
        })
    return breadcrumbs_list
