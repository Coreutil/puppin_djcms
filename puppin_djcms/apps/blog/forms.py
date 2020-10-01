# -*- coding: utf-8 -*-

from django import forms


class BlogPostAdminForm(forms.ModelForm):

    current_user = None

    def __init__(self, *args, **kwargs):
        super(BlogPostAdminForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['author'].initial = str(self.current_user)
        self.fields['author'].label_from_instance = lambda obj: '%s %s' % (
            obj.first_name, obj.last_name) if obj.first_name or obj.last_name else obj.username
