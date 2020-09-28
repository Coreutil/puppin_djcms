# -*- coding: utf-8 -*-

from django.db import models
# from django.urls import reverse


class BlogCategory(models.Model):

    name = models.CharField(u'Category name', blank=False, default='', max_length=100)
    slug = models.SlugField(u'Slug', blank=False, default='', max_length=255, unique=True)

    class Meta:
        app_label = 'blog'
        verbose_name_plural = 'Blog categories'

    # def get_absolute_url(self):
    #     return reverse()

    def __str__(self):
        return self.name

