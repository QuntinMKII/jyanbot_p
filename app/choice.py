# -*- coding: utf-8 -*-
import random

from app.base_app import base_app

class app(base_app):
    def __init__(self):
        self._keyword = '抽籤={選項},{選項}, ...'
        self._repr = '抽籤'
    
    def check(self, msg, **kwargs):
        return msg[:3] == '抽籤='
        
    def run(self, msg, **kwargs):
        s = msg[3:]
        if ',' in s:
            s = random.choice(s.split(','))
        return s