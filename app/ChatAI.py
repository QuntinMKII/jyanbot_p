# -*- coding: utf-8 -*-
import openai 
from app.base_app import base_app
with open('openai') as f:    
    openai.api_key = f.readline()


class app(base_app):
    def __init__(self):
        self._keyword = ['棄麻醬']
        self._repr = 'AI'
        self.group_id = ['C9ad15eba7c70c7d2e2c2a3468a532', 'C88c74492d7c2fd9db474ad122270e', 'C8b8d52d8fe5bdaf74aa87aa6fd66a0']
        self.room_id = ['Rc56e7f837167bcac41c6b76436c1c']
        self.flag = 0
        # self.context = ''
        # self.times = 0
        self._patchnote = '''ChatAI:
        230324:試著弄弄看
        '''
    def check(self, msg, **kwargs):
        if msg.split()[0] in self._keyword:
            self.flag = 1
        else :
            self.flag = 0
        return self.flag
        
    def run(self, msg, **kwargs):
        if self.flag:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": '回答限制在60字內'},                    
                    {"role": "system", "content": '你的角色是如同動漫角色般的16歲傲嬌女高中生，名字叫棄麻醬，回答問題前都會先語氣很差的把人當笨蛋罵，喜歡打日式麻將，但是打得不好'},
                    {"role": "user", "content": msg[4:]},
                     ],
                max_tokens=120,
                temperature=0.5,
                )
            return response['choices'][0]['message']['content'].strip() + ', token = '+ str(response['usage']['total_tokens'])
