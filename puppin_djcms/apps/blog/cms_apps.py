# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class BlogApp(CMSApp):
    name = 'Blog'
    app_name = 'blog'

    def get_urls(self, page=None, language=None, **kwargs):
        return ['puppin_djcms.apps.blog.urls']


apphook_pool.register(BlogApp)
