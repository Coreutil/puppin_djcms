# -*- coding: utf-8 -*-

from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models.blog_category import BlogCategory
from .models.blog_post import BlogPost


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name', )}
    fieldsets = (
        (None, {
            'fields': ('name', 'slug')
        }),
    )


admin.site.register(BlogCategory, BlogCategoryAdmin)


class BlogPostAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    list_display = ('headline', 'publication_datetime', 'get_categories', 'published')
    list_editable = ('published', )
    prepopulated_fields = {'slug': ('headline', )}
    fieldsets = (
        (None, {
            'fields': ('headline', 'slug', 'categories', 'publication_datetime', 'published', 'author',
                       'image')
        }),
    )


admin.site.register(BlogPost, BlogPostAdmin)

