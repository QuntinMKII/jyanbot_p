# -*- coding: utf-8 -*-
from app.base_app import base_app

class app(base_app):
    def __init__(self):
        self._keyword = 'myid'
        self._repr = 'myid'
    
    def check(self, msg, **kwargs):
        return msg == self._keyword
        
    def run(self, msg, room_id, group_id, user_id, **kwargs):
        mes = 'room_id:' + room_id + ',\n ' + 'group_id:' + group_id + ',\n ' + 'id:' + user_id
        return mes
