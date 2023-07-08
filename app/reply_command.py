# -*- coding: utf-8 -*-
import urllib

from app.base_app import base_app

class app(base_app):
    def __init__(self):
        self._keyword = ['指令']
        self._repr = '指令'
        self._url = 'command'
        self._run_once_at_begin = True
    
    def check(self, msg, **kwargs):
        return msg in self._keyword 
    
    def run(self, app_info, **kwargs):
        self.app_command = []
        for _k in app_info:
            self.app_command += _k if type(_k) is list else [_k]
        return self._host_url + self._url
    
    def web(self):
        return '<br>'.join(self.app_command)