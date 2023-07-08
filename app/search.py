# -*- coding: utf-8 -*-
import urllib

from app.base_app import base_app


class app(base_app):
    def __init__(self):
        self._keyword_0 = ['孤狗', '估狗']
        self._keyword_1 = ['是什麼', '是三小', '是啥', '是?']
        self._keyword_2 = ['google', 'GOOGLE']
        self._keyword_3 = ['維基']
        self._keyword_4 = ['wiki']
        self._keyword_5 = ['在哪？', '在哪', '在哪裡？', '在哪裡']
        self._keyword = [_+'{字串}' for _ in self._keyword_0 + self._keyword_2 +
                         self._keyword_3 + self._keyword_4] + ['{字串}'+_ for _ in self._keyword_1 + self._keyword_5]
        self._repr = 'search'
        self._search = ''
        self._search_engine = {
            'google_tw': 'https://www.google.com/search?hl=zh_tw&lr=lang_zh-TW&q={}',
            'google_us': 'https://www.google.com/search?hl=en_us&q={}',
            'wiki_zh': 'https://zh.wikipedia.org/wiki/{}',
            'wiki_en': 'https://en.wikipedia.org/wiki/{}',
            'google_map': 'https://www.google.com/maps/search/{}',
        }

    def check(self, msg, **kwargs):
        flag = False
        for _keyword in self._keyword_0:
            if msg[:len(_keyword)] == _keyword:
                flag = True
                self._search = msg[len(_keyword):]
                self._se = 'google_tw'

        for _keyword in self._keyword_1:
            if msg[-len(_keyword):] == _keyword:
                flag = True
                self._search = msg[:-len(_keyword)]
                self._se = 'google_tw'
                if len(self._search) == 1:
                    flag = False

        for _keyword in self._keyword_2:
            if msg[:len(_keyword)] == _keyword:
                flag = True
                self._search = msg[len(_keyword):]
                self._se = 'google_us'

        for _keyword in self._keyword_3:
            if msg[:len(_keyword)] == _keyword:
                flag = True
                self._search = msg[len(_keyword):]
                self._se = 'wiki_zh'

        for _keyword in self._keyword_4:
            if msg[:len(_keyword)] == _keyword:
                flag = True
                self._search = msg[len(_keyword):]
                self._se = 'wiki_en'

        for _keyword in self._keyword_5:
            if msg[-len(_keyword):] == _keyword:
                flag = True
                self._search = msg[:-len(_keyword)]
                self._se = 'google_map'

        if self._search in ['', ' ']:
            flag = False

        return flag

    def run(self, **kwargs):
        if self._search[0] == ' ':
            self._search = self._search[1:]
        return self._search_engine[self._se].format(urllib.parse.quote(self._search))
        """ TODO:
        第一個連結
        """
