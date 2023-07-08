# -*- coding: utf-8 -*-
from selenium import webdriver
import time

from app.base_app import base_app

class app(base_app):
        
    def __init__(self):
        self._keyword = "meme={文字},{meme類別}"
        self._repr = "meme"
        self.memetype={'是個笑話':'https://imgflip.com/memegenerator/155988880/Am-I-a-joke-to-you'}
        
    def check(self, msg, **kwargs):
        if 'meme=' in msg[:5]:
            return 2

    def run(self, msg, **kwargs):
        s = msg[5:].split(',')
        text = s[0]
        linktype = s[1]
        driver = webdriver.PhantomJS()
        driver.get(self.memetype[linktype])
        driver.find_element_by_class_name('mm-text').send_keys(u'%s'%text)
        # for private meme generate
        driver.find_element_by_class_name('gen-private').click()
        driver.find_element_by_css_selector('div.mm-generate.b.but').click()
        time.sleep(1)
        imglink = driver.find_element_by_css_selector('a.img-download.l.but').get_property('href')
        '''
        # for poblic meme generate(will last longer but public?)
        driver.find_element_by_css_selector('div.mm-generate.b.but').click()
        time.sleep(1)
        imglink = driver.find_element_by_css_selector('input.img-code.link').get_attribute('value')+'.jpg'        
        '''
        driver.close()
        return imglink
    
