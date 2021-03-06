# -*- coding: utf-8 -*-

from django.views.generic import DetailView
from django.views.generic.dates import ArchiveIndexView
from django.utils import timezone

from .models.blog_post import BlogPost
from .settings import ARCHIVE_POSTS_PAGINATE_BY


class BlogArchiveView(ArchiveIndexView):
    allow_empty = True
    date_field = 'publication_datetime'
    model = BlogPost
    paginate_by = ARCHIVE_POSTS_PAGINATE_BY

    def get_queryset(self):
        qs = super(BlogArchiveView, self).get_queryset()
        qs = qs.filter(published=True,
                       publication_datetime__lte=timezone.now())

        if 'category_slug' in self.kwargs:
            qs = qs.filter(categories__slug=self.kwargs['category_slug'])

        if 'year' in self.kwargs:
            qs = qs.filter(publication_datetime__year=self.kwargs['year'])

        return qs

    # def get_context_data(self, *, object_list=None, **kwargs):


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_queryset(self):
        qs = super(BlogPostDetailView, self).get_queryset()
        qs = qs.filter(published=True,
                       publication_datetime__lte=timezone.now())
        return qs


