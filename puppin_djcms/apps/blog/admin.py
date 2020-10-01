# -*- coding: utf-8 -*-

from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .forms import BlogPostAdminForm
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
    form = BlogPostAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(BlogPostAdmin, self).get_form(request, obj, *kwargs)
        form.current_user = request.user.id if request.user else None
        return form


admin.site.register(BlogPost, BlogPostAdmin)

