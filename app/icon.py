# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 09:54:42 2019

@author: quntin
"""
from flask import render_template
from oauth2client.service_account import ServiceAccountCredentials
from apiclient import discovery
from app.base_app import base_app
from datetime import datetime
import urllib
import requests
import json

debug = False


class app(base_app):

    def __init__(self):
        self._keyword = ['新增表符:{關鍵字},{圖片網址}', '移除表符:{關鍵字}', '刪除表符:{關鍵字}', 'iconlist', '{關鍵字}']
        self.group_id = ['C9ad1b5ea7c70c7d2e2c2a34687a532', 'C88c74492d7cc826fd9db474ad122270e', 'C8b8d52d8fe5bdaf74aa87aa6f2e6a0']
        self.room_id = ['Rc56e837167bca56c41c6b764326c1c']
        self.mode = 0
        self._url = 'iconlist'
        self._rank_url = 'icon_rank'
        self.SCOPES_SS = ['https://spreadsheets.google.com/feeds']
        self.credspath_logger = 'creds.json'
        self.ss_id = '1OMUFtHf5P8xAodFYc3bkvFApudhtnsMELN3SfzHX'    
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.credspath_logger, self.SCOPES_SS)
        self.service_ss = discovery.build('sheets','v4',credentials=creds)
        
        self.icon_dict = self.get_icon_dict()
        self._patchnote = '''icon:
            
            200711:新增支援聊天室roomid篩選條件
            200716:新增patchnote功能
            '''

    def check(self, msg, group_id, room_id, **kwargs):
        flag = 0
        if group_id in self.group_id:
            if msg in self.icon_dict.keys():
                flag = 2
                self.mode = 0
            if msg[:5] == '新增表符:':
                flag = 1
                self.mode = 1
            # if msg[:5] == '移除表符:' or msg[:5] == '刪除表符:':
            #     flag = 1
            #     self.mode = 3
        if room_id in self.room_id:
            if msg in self.icon_dict.keys():
                flag = 2
                self.mode = 0            
        if msg == 'iconlist':
            flag = 1
            self.mode = 2
        # if msg == '表符排行':
        #     flag = 1
        #     self.mode = 4
        return flag
        
    def run(self, msg, **kwargs):
        if self.mode == 0:
            message = self.icon_dict[msg]            
        
            self._repr = '貼表符 %s' % msg
            return message
            #old version
            # response = requests.get('http://dat-bot-api.herokuapp.com/icon/' + urllib.parse.quote_plus(msg))
            # self.icon_history_insert(msg)
            # self._repr = '貼表符 %s' % msg
            # return message
            
        elif self.mode == 1:
            # key, imglink = self.new_icon_str_parse(msg[5:])
            body = {'values': [[key, imglink]]}
            self.service_ss.spreadsheets().values().append(spreadsheetId=ss_id, range='試算表1', valueInputOption='USER_ENTERED', body=body).execute()                               
            mes = self.icon_insert(key, imglink)
            self._repr = '新表符'
            return mes
        
        elif self.mode == 2:
            mes = ''
            self.icon_dict = self.get_icon_dict()
            for k in self.icon_dict.keys():
                mes = mes + k + ', '
            self._repr = 'iconlist'
            return self._host_url + self._url
        
        # elif self.mode == 3:
        #     key = msg[5:].strip()
        #     mes = self.icon_delete(key)
        #     self._repr = '刪表符'
        #     return mes

        # elif self.mode == 4:
        #     self._repr = '表符排行'
        #     mes = self.get_icon_ranking()
        #     return mes

    def get_icon_dict(self):
        re = self.service_ss.spreadsheets().values().get(
        spreadsheetId=self.ss_id,
        range='工作表1', 
        majorDimension="COLUMNS",).execute()        
        d = dict(zip(re['values'][0],re['values'][1]))
        #re['values'] = [[keyname],[imglink]]
        return d

    # def get_img_link_list(self):
    #     my_database.cursor.execute('select imglink from icon')
    #     key_rows = my_database.cursor.fetchall()
    #     il = []
    #     for row in key_rows:
    #         il.append(row[0])
    #     return il

    # def refresh_key_list(self):
    #     self.icon_dict.keys() = self.get_key_list()

    # def refresh_img_link_list(self):
    #     self.img_link_list = self.get_img_link_list()

    # def new_icon_str_parse(self, s):
    #     lists = s.strip().split(',')
    #     if len(lists) == 2:
    #         key = lists[0]
    #         img_link = lists[1]
    #         return key, img_link

    # def get_img_link(self, keystr):
    #     my_database.cursor.execute('select imglink from icon where keyword = %s;', (keystr,))
    #     message = my_database.cursor.fetchone()
    #     return message

    def icon_insert(self, new_key, new_img_link):
        if new_key in self.icon_dict.keys():
            return '已有此表符'
        else:

            self.icon_dict[new_key] = new_img_link
            return '新增成功'

    # def icon_delete(self, key):
    #     if key in self.icon_dict.keys():
    #         my_database.cursor.execute("DELETE FROM icon WHERE keyword = %s;", (key,))
    #         my_database.conn.commit()
    #         self.icon_dict.keys().remove(key)
    #         return '移除成功'
    #     else:
    #         return '無此表符'

    # def icon_history_insert(self, key):
    #     if key in self.icon_dict.keys():
    #         my_database.cursor.execute(
    #             "INSERT INTO icon_history (keyword, record_time) VALUES (%s, %s);",
    #             (key, datetime.now()))
    #         my_database.conn.commit()

    # def get_icon_ranking(self):
    #     my_database.cursor.execute('select * from icon_ranking fetch first 5 rows only;')
    #     ranking_rows = my_database.cursor.fetchall()
    #     message = ""
    #     for _keywords, _counting in ranking_rows:
    #         message += _keywords + ", 使用次數: " + str(_counting) + "\n"
    #     return message

    # def get_all_list_ranking(self):
    #     my_database.cursor.execute('select * from icon_all_ranking_list;')
    #     ranking_rows = my_database.cursor.fetchall()
    #     return [{'keyword': _keywords, 'link': _img_link, 'counting': _counting}
    #             for _keywords, _img_link, _counting in ranking_rows]

    
    def web(self):
        # _icon = {}
        # for keyword, link in zip(self.icon_dict.keys(), self.img_link_list):
        #     if link in _icon:
        #         _icon[link] += ', ' + keyword
        #     else:
        #         _icon[link] = keyword
        icon_list = [self.icon_dict.keys(),self.icon_dict.items()]
        return render_template("iconlist.html", iconlist=icon_list)
