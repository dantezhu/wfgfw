# -*- coding: utf-8 -*-

__version__ = '0.1.1'

from .wfgfw import DFAFilter
try:
    from .flask_wfgfw import FlaskWFGFW
except:
    pass
