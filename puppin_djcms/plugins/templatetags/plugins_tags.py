# -*- coding: utf-8 -*-

from django import template

from puppin_djcms.utils import get_breadcrumbs_list


register = template.Library()


@register.inclusion_tag('breadcrumbs.html', takes_context=True)
def breadcrumbs_list(context):
    context.update({'breadcrumbs': get_breadcrumbs_list(context['request'])})
    return context
