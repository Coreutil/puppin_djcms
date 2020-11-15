# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models.footer_plugin import Footer
from .models.latest_blog import LatestBlog
from .models.page_head_plugin import PageHead
from puppin_djcms.apps.blog.models.blog_post import BlogPost


class FooterPlugin(CMSPluginBase):
    model = Footer
    name = u'Footer'
    module = u'Specific plugins'
    render_template = 'footer_plugin/footer_plugin.html'

    def render(self, context, instance, placeholder):
        return super(FooterPlugin, self).render(context, instance, placeholder)


class PageHeadPlugin(CMSPluginBase):
    model = PageHead
    name = u'Page Head'
    module = u'Specific plugins'
    render_template = 'page_head_plugin/page_head_plugin.html'


class LatestBlogPlugin(CMSPluginBase):
    model = LatestBlog
    name = u'Latest Blog'
    module = u'Specific plugins'
    render_template = 'latest_blog_plugin/latest_blog.html'

    def render(self, context, instance, placeholder):
        context = super(LatestBlogPlugin, self).render(context, instance, placeholder)
        if instance.posts_number:
            context.update({
                'recent_posts': BlogPost.published_objects.all()[:instance.posts_number]
            })
        return context


plugin_pool.register_plugin(FooterPlugin)
plugin_pool.register_plugin(PageHeadPlugin)
plugin_pool.register_plugin(LatestBlogPlugin)
