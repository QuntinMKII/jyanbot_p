# -*- coding: utf-8 -*-
''' TODO:
# 提醒:
if event.message.text[:2] in ['提醒']:
    s = event.message.text.split(' ')
    if len(s) != 3:
        return 0
    try:
        _ = float(s[1])
    except:
        return 0
    if event.source.type=='user':
        _id = event.source.user_id
    
    if event.source.type=='group':
        _id = event.source.group_id
    
    line_bot_api.push_message(
        _id, 
        TextSendMessage(text='好'))
    time.sleep(float(s[1]))
    line_bot_api.push_message(
        _id, 
        TextSendMessage(text=s[2]))
    
    return 0
'''