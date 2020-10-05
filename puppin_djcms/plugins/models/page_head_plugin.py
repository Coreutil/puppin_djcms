# -*- coding: utf-8 -*-

from cms.models.pluginmodel import CMSPlugin
from django.db import models

from filer.fields.image import FilerImageField


class AbstractPageHead(CMSPlugin):
    image = FilerImageField(verbose_name=u'Image', blank=True, null=True, on_delete=models.SET_NULL,
                            related_name='page_head_image')
    social_panel = models.BooleanField(u'Social panel', default=False)
    breadcrumbs = models.BooleanField(u'Breadcrumbs', default=False)

    class Meta:
        abstract = True


class PageHead(AbstractPageHead):

    class Meta:
        abstract = False
