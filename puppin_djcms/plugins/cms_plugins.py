# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models.footer_plugin import Footer


class FooterPlugin(CMSPluginBase):
    model = Footer
    name = u'Footer'
    module = u'Specific plugins'
    render_template = 'footer_plugin/footer_plugin.html'

    def render(self, context, instance, placeholder):
        return super(FooterPlugin, self).render(context, instance, placeholder)


plugin_pool.register_plugin(FooterPlugin)
