# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import os
from app.base_app import base_app

'''
reference
https://medium.com/@op880623/%E5%9C%A8-heroku-%E4%BD%BF%E7%94%A8-phantomjs-d0592615b353
可能要先看這個
https://medium.com/@mikelcbrowne/running-chromedriver-with-python-selenium-on-heroku-acc1566d161c
注意build的網址有錯
https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-chromedriver
https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-google-chrome
'''

class app(base_app):
        
    def __init__(self):
        self._keyword = "meme={meme類別},{文字}"
        self._repr = "meme"
        self.memetype={'是個笑話' : 'https://imgflip.com/memegenerator/155988880/Am-I-a-joke-to-you',
                       '腦內組成' : 'https://imgflip.com/memegenerator/200799770/Whats-on-your-mind',
                       '再也不' : 'https://imgflip.com/memegenerator/259455611/no-more-majhan',
                       }
        
    def check(self, msg, **kwargs):
        if 'meme=' in msg[:5]:
            return 2

    def run(self, msg, **kwargs):
        s = msg[5:].split(',')
        text = s[1:]
        linktype = s[0]
        opts = Options()
        opts.add_argument('--headless')  # 無頭chrome
        opts.add_argument('--disable-gpu')        
        driver = webdriver.Chrome('/app/.chromedriver/bin/chromedriver', chrome_options=opts)
        driver.get(self.memetype[linktype])        
        act = ActionChains(driver)
        
        if linktype == '腦內組成':
            driver.find_element_by_css_selector("#mm-settings > div.mm-boxes > div:nth-child(1) > div.mm-text-wrap > textarea").send_keys(u'%s'%text[0])
            driver.find_element_by_css_selector("#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-text-wrap > textarea").send_keys(u'%s'%text[1].replace('\n', os.linesep))
            
            topframe = driver.find_element_by_css_selector(
                    "#mm-preview-outer > div.mm-preview > div:nth-child(3)")
            topE = driver.find_element_by_css_selector(
                    "#mm-preview-outer > div.mm-preview > div:nth-child(3) > div.wrapE > div")
            topframe.click()
            act.move_to_element(topframe)
            act.drag_and_drop_by_offset(topframe,0,100)
            act.move_to_element(topE)
            act.drag_and_drop_by_offset(topE,-320,0)
            
            botframe = driver.find_element_by_css_selector(
                    "#mm-preview-outer > div.mm-preview > div:nth-child(2)")
            botE = driver.find_element_by_css_selector(
                    "#mm-preview-outer > div.mm-preview > div:nth-child(2) > div.wrapE > div")
            act.move_to_element(botE)
            act.drag_and_drop_by_offset(botE,-140,0)
            act.move_to_element(botframe)
            act.drag_and_drop_by_offset(botframe,80,-170)
            act.perform()
            
            botcolorbtn = driver.find_element_by_css_selector('#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-font-options > div.color-picker.mm-font-color-picker > div.color-btn')
            botcolorbtn.click()                                                 
            botcolor = driver.find_element_by_css_selector('#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-font-options > div.color-picker.mm-font-color-picker > div.color-popup.ibox > div.color-panel > input')
            botcolor.clear()
            botcolorbtn.click()
            botcolor.send_keys('#ff0000')
            botframe.click()                  
            
            botoutlinecolorbtn = driver.find_element_by_css_selector(
                    "#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-font-options > div.color-picker.mm-outline-color-picker > div.color-btn")
            botoutlinecolorbtn.click()
            botoutlinecolor = driver.find_element_by_css_selector('#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-font-options > div.color-picker.mm-outline-color-picker > div.color-popup.ibox > div.color-panel > input')
            botoutlinecolor.clear()
            botoutlinecolorbtn.click()
            botoutlinecolor.send_keys('#f4b7f2')
            botframe.click()        
        
        elif linktype == '再也不':
            
            driver.find_element_by_css_selector("#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-text-wrap > textarea").send_keys(u'%s'%text[0])
            
            botframe = driver.find_element_by_css_selector(
                    "#mm-preview-outer > div.mm-preview > div:nth-child(2)")
            botE = driver.find_element_by_css_selector(
                    "#mm-preview-outer > div.mm-preview > div:nth-child(2) > div.wrapE > div")
            botframe.click()
            act.move_to_element(botE)
            act.drag_and_drop_by_offset(botE,-321,0)
            act.move_to_element(botframe)
            act.drag_and_drop_by_offset(botframe,134.5,-1.5)
            act.perform()
                        
            botcolorbtn = driver.find_element_by_css_selector('#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-font-options > div.color-picker.mm-font-color-picker > div.color-btn')
            botcolorbtn.click()                                                 
            botcolor = driver.find_element_by_css_selector('#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-font-options > div.color-picker.mm-font-color-picker > div.color-popup.ibox > div.color-panel > input')
            botcolor.clear()
            botcolorbtn.click()
            botcolor.send_keys('#ebf3f4')
            botframe.click()                  
            
            botoutlinecolorbtn = driver.find_element_by_css_selector(
                    "#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-font-options > div.color-picker.mm-outline-color-picker > div.color-btn")
            botoutlinecolorbtn.click()
            botoutlinecolor = driver.find_element_by_css_selector('#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-font-options > div.color-picker.mm-outline-color-picker > div.color-popup.ibox > div.color-panel > input')
            botoutlinecolor.clear()
            botoutlinecolorbtn.click()
            botoutlinecolor.send_keys('#58716d')
            botframe.click()
            
            botsettings = driver.find_element_by_css_selector('#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-font-options > div.mm-font-options-btn-wrap > div.l.but.mm-font-options-btn')
            botsettings.click()
            driver.find_element_by_css_selector('#mm-settings > div.mm-boxes > div:nth-child(2) > div.mm-font-options > div.mm-font-options-btn-wrap > div.mm-font-options-popup.ibox > div.mm-font-opt.mm-font-bold-wrap > div > svg').click()
            botsettings.click()
            
        else:   
            driver.find_element_by_class_name('mm-text').send_keys(u'%s'%text[0])
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
    
