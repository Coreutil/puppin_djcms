# -*- coding: utf-8 -*-

from django.conf import settings


def get_setting(name, default):
    """
    A little helper for fetching global settings with a common prefix.
    """
    parent_name = 'BLOG_{0}'.format(name.upper())
    return getattr(settings, parent_name, default)


RECENT_POSTS_NUM = get_setting('RECENT_POSTS_NUM', 4)
ARCHIVE_POSTS_PAGINATE_BY = get_setting('ARCHIVE_POSTS_PAGINATE_BY', 9)
