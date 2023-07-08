# -*- coding: utf-8 -*-
import mistune

from app.base_app import base_app

class app(base_app):
    def __init__(self):
        self._keyword = ['readme']
        self._repr = 'readme'
        self._url = 'readme'
        self._run_once_at_begin = True
        self.markdown = mistune.Markdown()
    
    def check(self, msg, **kwargs):
        return msg in self._keyword 
    
    def run(self, app_info, **kwargs):
        s = ''.join(open('README.md', 'r', encoding='utf8').readlines())
        s += '\n---\n## 使用者\n'
        for k in app_info:
            if type(k) is not list:
                k = [k]
            for _k in k:
                s += '* {}\n'.format(_k.replace('*', '\*'))
        self._web = self.markdown(s)
        return self._host_url + self._url
    
    def web(self):
        return self._web