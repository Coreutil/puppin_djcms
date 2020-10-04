# -*- coding: utf-8 -*-

from cms.models.pluginmodel import CMSPlugin
from django.db import models

from puppin_djcms.utils import get_current_year


COPYRIGHT_SYMBOL = '©'
COPYRIGHT_START_YEAR = 2008


class AbstractFooter(CMSPlugin):
    copyright_author = models.CharField(u'Copyright author', blank=False, default='', max_length=255)
    social_panel = models.BooleanField(u'Social panel', default=False)
    scrollup_button = models.BooleanField(u'Scroll up button', default=False)
    dark_background = models.BooleanField(u'Dark background', default=False)
    border_top = models.BooleanField(u'Top border', default=False)

    @property
    def copyright(self):
        return '%s %s %s-%s - All Rights Reserved' % (COPYRIGHT_SYMBOL, self.copyright_author,
                                                      COPYRIGHT_START_YEAR, get_current_year())

    class Meta:
        abstract = True


class Footer(AbstractFooter):

    class Meta:
        abstract = False