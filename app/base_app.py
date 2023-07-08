# -*- coding: utf-8 -*-

class base_app:
    _keyword = None
    _repr = None
    _url = None
    _patchnote = None
    _host_url = 'https://jyanbot.onrender.com/'
    _run_once_at_begin = False
    
    def __init__(self):
        pass
    
    def __repr__(self):
        return self._repr
    
    def check(self, msg, **kwargs):
        return False
    
    def run(self, msg, **kwargs):
        return ''
    
    @property
    def keyword(self):
        return self._keyword
    
    def web(self):
        return None
    
    @property
    def patchnote(self):
        return self._patchnote    

    @property
    def url(self):
        return self._url
