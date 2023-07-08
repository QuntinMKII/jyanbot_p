# -*- coding: utf-8 -*-
import requests
import json


from app.base_app import base_app
with open('air') as f:    
    apikey = f.readline()

url = 'https://data.epa.gov.tw/api/v1/aqx_p_432?offset=0&limit=80&api_key=%s'%apikey
# EPA空品 關鍵字 空品:
class app(base_app):
    def __init__(self):
        self._keyword = '*空品:{地點}'
        self.pollutants = ['AQI', 'CO', 'NO2', 'O3', 'SO2', 'PM10', 'PM2.5']
        
    def check(self, msg, **kwargs):
        return '空品:' in msg
        
    def run(self, msg, **kwargs):
        #用戶輸入的訊息=msg，格式是"空品:{site}"
        s = msg
        site = s.split(':')[1]
        location_str = requests.get(url)
        locations = json.loads(location_str.text)
        for location in locations['records']:
            #找符合站名的字串
            if location['SiteName'] == site:
                text_q=site+'\n'
                for p in self.pollutants:
                    text_q=text_q+p+': '+location[p]+'\n'
                self._repr = '空品'
                return text_q[:-1]
                
        self._repr = '空品_查無此站'
        return 'Cannot find %s Site'%site