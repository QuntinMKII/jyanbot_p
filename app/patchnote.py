# -*- coding: utf-8 -*-
import urllib

from app.base_app import base_app

class app(base_app):
    def __init__(self):
        self._keyword = ['patchnote']
        self._repr = 'patchnote'
        self._url = 'patchnote'
        self._run_once_at_begin = True
        self._patchnote ='''patchnote:
        200716:仿照reply_command 製作by quntin
        '''
    
    def check(self, msg, **kwargs):
        return msg in self._keyword 
    
    def run(self, app_patchnote, **kwargs):
        self.app_patchnote_list = []
        for _p in app_patchnote:
            _p = _p.replace('\n','<br>')
#            print (type(_p))
            self.app_patchnote_list += _p if type(_p) is list else [_p]
        return self._host_url + self._url
    
    def web(self):
        return '<br><br>'.join(self.app_patchnote_list)
    
    
