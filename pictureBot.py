#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telepot

class pictureBot:
    def __init__(self, telegram_bot):
        self.telegram = telegram_bot
        self.telegram.start(self.telegram_on_chat, self.telegram_on_callback_query)
    
    def telegram_on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        print('Callback Query:', query_id, from_id, query_data, str(msg))

        self.telegram.answer_callback_query(query_id, text='Got it')

    def telegram_on_chat(self, msg):
        print('telegram calback called: ' + str(msg))
        content_type, _, chat_id = telepot.glance(msg)

        if content_type == 'document' and msg['document']['mime_type'] == 'image/jpeg':
            self.telegram.download_picture(msg['document']['file_id'])

        elif content_type == 'photo':
            biggestPicture = {'size': -1}
            for photoid in msg['photo']:
                if photoid['file_size'] > biggestPicture['size']:
                    biggestPicture['size'] = photoid['file_size']
                    biggestPicture['id'] = photoid['file_id']
            print (biggestPicture)
            if 'id' in biggestPicture:
                self.telegram.download_picture(biggestPicture['id'])
        
        elif content_type == 'location':
            self.telegram.send_message(chat_id, 'thanks, but why?')
        
        elif content_type == 'text' and msg['text'] == 'test':
            self.telegram.send_inline_keyboard(chat_id, 'test')

        else:
            self.telegram.send_message(chat_id, 'Hallo ' + msg['from']['first_name'] + ' please send an image or a photo of your Chili')
