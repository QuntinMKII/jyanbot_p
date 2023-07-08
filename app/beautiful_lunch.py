# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 09:54:42 2019

@author: quntin
"""
import random
import time

from app.base_app import base_app
from datetime import datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials
from apiclient import discovery

debug = False


class app(base_app):

    def __init__(self):
        self._keyword = ['美食','新竹美食','今日美食','今日午餐','午餐','誰開']
        self.group_id = ['C9ad15eb5ea7c70c7d2e2c2a3468a532', 'C88c74492d7cc826d9db474ad122270e', 'C8b8d52d8fe5bdaf74aa87aa6fd2e6a0']
        self.room_id = ['Rc56e7f837167bca56c41c6b76326cc']
        self.SCOPES_SS = ['https://spreadsheets.google.com/feeds']
        self.credspath_logger = 'creds.json'
        self.ss_id = '1IZP2fgi3FnLjPwRgzqjnYMVzlCM2jvpq3seFLdkG'
        self._patchnote = '''美食:
            20080?:完成大致體系，結合估狗表單連動
            200812:新增快速填入本日午餐功能，表單抽籤系統連動，誰開車功能
            201109:因為gsuite被砍帳號不見了重弄creds
            '''

        self._last_time = None
        self._driver = None

    def check(self, msg, group_id, room_id, **kwargs):
        flag = 0
        if group_id in self.group_id:
            if msg.replace(':','=').split('=')[0].replace('天','日') in self._keyword:
                flag = 1
        if room_id in self.room_id:
            if msg.replace(':','=').split('=')[0].replace('天','日') in self._keyword:
                flag = 1                                
        return flag
        
    def run(self, msg, **kwargs):
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.credspath_logger, self.SCOPES_SS)
        service_ss = discovery.build('sheets','v4',credentials=creds)
        key = msg.replace(':','=').split('=')[0]
        
        if key in ['美食','新竹美食']:
            re = service_ss.spreadsheets().values().get(
            spreadsheetId=self.ss_id,
            range='美食!A1', 
            majorDimension="COLUMNS",).execute()
            mes = re['values'][0][0]
            return mes
        elif key in ['誰開']:
            if (self._last_time is None
                    or datetime.now() - self._last_time > timedelta(hours=12)):
                self._last_time = datetime.now()
                self._driver = random.choice(['仕延', 'U醬PAPA'])
            return self._driver
        elif key.replace('天','日') in ['今日美食','今日午餐', '午餐']:
            if key == '午餐':
                re = service_ss.spreadsheets().values().get(
                spreadsheetId=self.ss_id,
                range='美食!C1',
                majorDimension="COLUMNS",).execute()
                mes = re['values'][0][0]
                return mes
            else:
                timestamp = datetime.now().strftime('%m%d ')
                re = service_ss.spreadsheets().values().get(
                        spreadsheetId=self.ss_id,
                        range='美食!B1',
                        majorDimension="COLUMNS",).execute()
                if 'values' in re:
                    olddata = re['values'][0][0] + '\n'
                else :
                    olddata = ''
                values = [[olddata +
                           timestamp + 
                           msg.replace(':','=').split('=')[1]]]
                body = {'values': values}
                re = service_ss.spreadsheets().values().update(
                        spreadsheetId=self.ss_id, range='美食!B1', valueInputOption='USER_ENTERED', body=body).execute()
                return random.choice(['新增成功，這間這麼難吃也要吃啊',
                        '新增成功，是不是變難吃了',
                        '新增成功，要不要順便掛號',
                        '新增成功，新竹水準',
                        '新增成功，怎麼樣果然很難吃吧'])
