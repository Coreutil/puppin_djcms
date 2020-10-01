# -*- coding: utf-8 -*-

from django import template


register = template.Library()


@register.simple_tag(name='user_name')
def get_user_name(user):
    if user and user.first_name or user.last_name:
        return '%s %s' % (user.first_name, user.last_name)
    return user.username
