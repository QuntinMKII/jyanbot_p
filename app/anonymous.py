# -*- coding: utf-8 -*-
'''
    if event.source.type=='user':
        if event.message.text[:4] == '偷偷說:':
            s = event.message.text
            line_bot_api.push_message(
                    group_id['our'],
                    TextSendMessage(text = s)
                )
            return '偷偷說'
    
    if event.source.type=='user':
        if event.message.text[:4] == '偷偷貼:':
            s = event.message.text
            s = s[4:]
            line_bot_api.push_message(
                    group_id['our'],
                    ImageSendMessage(original_content_url=s,
                                     preview_image_url=s)
                )
            line_bot_api.push_message(
                    group_id['our'],
                    TextSendMessage(text = '偷偷貼')
                )
            return '偷偷貼'
'''