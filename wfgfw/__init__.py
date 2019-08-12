__version__ = '0.1.7'

from .wfgfw import DFAFilter
try:
    from .flask_wfgfw import FlaskWFGFW
except:
    pass
