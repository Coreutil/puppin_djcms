# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models.footer_plugin import Footer
from .models.page_head_plugin import PageHead


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


plugin_pool.register_plugin(FooterPlugin)
plugin_pool.register_plugin(PageHeadPlugin)
