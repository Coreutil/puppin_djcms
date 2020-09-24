# -*- coding: utf-8 -*-

import sys
from .defaults import *

"""
    Settings: 
    1. Default settings are in config/defaults.py. If a default value cannot be specified, the parameter is assigned 
the NotImplemented value. This parameter must be overridden in the local.py config.
    2. Custom settings are in config/local.py.     
"""

exec(open(os.path.dirname(__file__) + '/local.py').read())

DEPRECATED = set()


def validate_config():
    errors = []
    for n, v in globals().items():
        # Some settings are required to be overridden
        if v is NotImplemented:
            errors.append(n)

        if n in DEPRECATED:
            print('WARNING: config parameter %s is deprecated' % n, file=sys.stderr)

    if errors:
        raise NameError(errors)
