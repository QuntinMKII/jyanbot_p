# -*- coding: utf-8 -*-
from app.base_app import base_app

class app(base_app):
    def __init__(self):
        self._keyword = ['{圖片網址}']
        self._repr = 'open_image'
    
    def check(self, msg, **kwargs):
        if msg[:4].lower() == 'http':
            if msg[-4:].lower() in ['.jpg', '.png']:
                return 2
        return False
        
    def run(self, msg, **kwargs):
        return msg