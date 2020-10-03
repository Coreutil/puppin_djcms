# -*- coding: utf-8 -*-

from django import template
from django.db.models import Count
from django.utils import timezone

from ..models.blog_post import BlogPost
from ..models.blog_category import BlogCategory


register = template.Library()


@register.simple_tag(name='user_name')
def get_user_name(user):
    if user and user.first_name or user.last_name:
        return '%s %s' % (user.first_name, user.last_name)
    return user.username


@register.inclusion_tag('blog/categories_list.html', takes_context=True, name='categories_list')
def get_all_categories(context):
    categories = BlogCategory.objects.filter(
        blog_post__published=True, blog_post__publication_datetime__lte=timezone.now()
    ).annotate(num_posts=Count('blog_post'))
    context.update({'categories': categories})
    return context


@register.inclusion_tag('blog/recent_posts_list.html', takes_context=True, name='recent_posts')
def get_recent_posts(context):
    posts = BlogPost.objects.filter(
        published=True, publication_datetime__lte=timezone.now())[:4]
    context.update({'recent_posts': posts})
    return context
