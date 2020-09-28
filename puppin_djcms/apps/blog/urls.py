# -*- coding: utf-8 -*-

from django.urls import path, re_path

from .views import BlogArchiveView


urlpatterns = [
    re_path(r'^$', BlogArchiveView.as_view(), name='archive'),
    re_path(r'^(?P<year>[0-9]{4})/$', BlogArchiveView.as_view(), name='archive'),
    re_path(r'^category/(?P<category_slug>[^/]+)/$', BlogArchiveView.as_view(), name='archive'),
    re_path(r'^category/(?P<category_slug>[^/]+)/(?P<year>[0-9]{4})/$', BlogArchiveView.as_view(), name='archive')
]

