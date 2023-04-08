__version__ = '0.1.8'

from .wfgfw import DFAFilter
try:
    from .flask_wfgfw import FlaskWFGFW
except:
    pass
