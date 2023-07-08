# -*- coding: utf-8 -*-
#import re
#from bs4 import BeautifulSoup as bs
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#chrome_options = Options() # 啟動無頭模式
#chrome_options.add_argument('--headless')  # 規避google bug

from app.base_app import base_app

class app(base_app):
    def __init__(self):
        self._keyword = '何切={牌面}'
        self._repr = '何切'
        self.id = ['C9ad15eb5ea7c77d2e2c2a34687a532']
        self.tail = [['m', '萬'],['p', '筒'],['s', '條'],['p', '餅'],['s', '索'],['1z', '東'],['2z', '南'],['3z', '西'],['4z', '北'],['5z', '白'],['6z', '發'],['7z', '中']]
    
    def check(self, msg, type, id, **kwargs):
        return id in self.id and '何切' in msg[:2] and len(msg)>=5
        
    def run(self, msg, **kwargs):
        s = msg
        pai = s[3:]
        for s1, s2 in self.tail:
            pai = pai.replace(s2, s1)
        driver = webdriver.PhantomJS()
        #driver.implicitly_wait(10)
        driver.get('https://tenhou.net/2/?q='+pai)
        res = driver.find_element_by_id('m2').text
        res = res.split(pai)[1][1:]
        for s1, s2 in self.tail:
            res = res.replace(s1, s2)
        for s1 in ['萬', '筒', '條']:
            for s2 in '123456789':
                for s3 in '123456789':
                    res = res.replace(s2+s1+s3+s1, s2+s3+s1)
        driver.quit()
        return res