#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
配置:
    WFGFW_KEYWORD_FILES = ['xx', 'yy']  需要解析的字典列表
"""

from flask import g
from .wfgfw import DFAFilter


class FlaskWFGFW:
    """作为flask插件
    """
    _filter = None

    def __init__(self, app=None):
        self._filter = DFAFilter()

        if app:
            self.init_app(app)

    def init_app(self, app):
        """安装到app
        """
        if app.config.get('WFGFW_KEYWORD_FILES'):
            for filename in app.config.get('WFGFW_KEYWORD_FILES'):
                self._filter.parse(filename)

        @app.before_request
        def inject_wfgfw():
            g.wfgfw = self._filter
