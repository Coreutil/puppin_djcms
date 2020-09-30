# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from filer.fields.image import FilerImageField

from cms.models.fields import PlaceholderField


class BlogPost(models.Model):
    headline = models.CharField(u'Headline', blank=False, default='', max_length=255)
    slug = models.SlugField(u'Slug', blank=False, default='', unique=True, max_length=255)
    categories = models.ManyToManyField('blog.BlogCategory', blank=False, related_name='blog_post',
                                        help_text=u'Please select one or more categories for this post')
    published = models.BooleanField(u'Published', default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_datetime = models.DateTimeField(u'Creation date', null=True, default=timezone.now)
    modified_datetime = models.DateTimeField(u'Last updated on', auto_now=True, editable=False)
    publication_datetime = models.DateTimeField(u'Publication date', default=timezone.now,
                                                help_text=u'The blog post will be published automatically once a '
                                                          u'publication date is specified')
    image = FilerImageField(on_delete=models.SET_NULL, blank=True, null=True, related_name='blog_post_image')
    post_content = PlaceholderField('post_content')

    objects = models.Manager()

    class Meta:
        app_label = 'blog'
        verbose_name_plural = 'Blog posts'
        ordering = ('-publication_datetime',)

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('blog:blog_post_detail', kwargs={'slug': self.slug})

    def get_categories(self):
        return ', '.join([str(category) for category in self.categories.all()])
