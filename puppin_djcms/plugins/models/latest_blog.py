# -*- coding: utf-8 -*-

from cms.models.pluginmodel import CMSPlugin
from django.db import models


DEFAULT_POSTS_NUMBER = 3


class AbstractLatestBlog(CMSPlugin):
    title = models.CharField(u'Title', max_length=128)
    posts_number = models.PositiveIntegerField(u'Number of posts', default=DEFAULT_POSTS_NUMBER)

    class Meta:
        abstract = True


class LatestBlog(AbstractLatestBlog):

    class Meta:
        abstract = False
