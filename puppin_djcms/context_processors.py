# -*- coding: utf-8 -*-
from .utils import get_basic_context


def puppin_settings(request):
    """
    Adds current project variables to the context
    """
    return get_basic_context(request)
