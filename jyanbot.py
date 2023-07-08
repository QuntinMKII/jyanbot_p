# -*- coding: utf-8 -*-
'''ssh -R quntinlinebot:80:localhost:5000 serveo.net'''

import os
from flask import Flask, send_from_directory
from flask import request
from flask import abort
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent
from linebot.models import TextMessage
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage
import app as line_app
import json

with  open('lineapi.json') as f:    
   apikey, handlerkey = json.load(f).values()


app = Flask(__name__,
            static_url_path='/web/static',
            static_folder='web/static',
            template_folder='web/templates')
line_bot_api = LineBotApi(apikey)
handler = WebhookHandler(handlerkey)
APP = {_: vars(line_app)[_].app() for _ in vars(line_app) if type(vars(line_app)[_])==type(line_app) and 'app' in vars(vars(line_app)[_])}
app_info = [_.keyword for _ in APP.values()]
app_patchnote = [_.patchnote for _ in APP.values() if _.patchnote is not None]
app_url = {APP[_].url: _ for _ in APP if APP[_].url is not None}
_ = [_app.run(msg='', type='', id='',user_id='', room_id='', group_id='', app_info=app_info, app_patchnote = app_patchnote) for _app in APP.values() if _app._run_once_at_begin]

debug_mes = False

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    if debug_mes:
        print("body:",body)
        app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return '200'

@app.route("/favicon.ico", methods=['GET', 'POST'])
def favicon_ico():
        return send_from_directory(os.path.join(app.root_path, 'web/static'), 'favicon.ico')

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if debug_mes:
        print('event.source:',event.source)
        print('source.type',event.source.type)
        print('Id',event.userId)
        print('source.userID',event.source.user_id)
        print('source.groupID',event.source.group_id)
        print('event.reply_token:', event.reply_token)
        print('event.message.text:', event.message.text)
    
    d = {
        'msg': event.message.text,
        'type': event.source.type,
        'id': vars(event.source)[event.source.type+'_id'],
        'user_id': event.source.user_id,
        'room_id': event.source.room_id if event.source.type == 'room' else '',
        'group_id': event.source.group_id if event.source.type == 'group' else '',
        'app_info': app_info,
        'app_patchnote': app_patchnote, 
    }
    
    reply = []
    for _app in APP.values():
        _flag = _app.check(**d)
        for _flag, _s in zip(_flag, _app.run(**d)) if type(_flag) is list else [[int(_flag), _app.run(**d)] if _flag else [0, '']]:
            if _flag == 1:
                reply += [TextSendMessage(text=_s)]
            if _flag == 2:
                _s = _s.replace('http:', 'https:')
                reply += [ImageSendMessage(original_content_url=_s, preview_image_url=_s)]
    
    if len(reply)>0:
        line_bot_api.reply_message(event.reply_token, reply)

@app.route("/<url>", methods=['GET', 'POST'])
def app_web(url):
    return APP[app_url[url]].web() if url in app_url else None

if __name__ == '__main__':
    app.run()
