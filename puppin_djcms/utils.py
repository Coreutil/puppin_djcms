# -*- coding: utf-8 -*-

from django.utils import timezone


def get_current_year():
    return timezone.now().year
