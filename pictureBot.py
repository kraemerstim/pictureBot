#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telepot

class pictureBot:
    def __init__(self, telegram_bot):
        self.telegram = telegram_bot
        self.telegram.start(self.telegram_callback)
    
    def telegram_callback(self, msg):
        content_type, chat_id = telepot.glance(msg)[0, 2]

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

        else:
            self.telegram.send_message(chat_id, 'Hallo ' + msg['from']['first_name'] + ' please send an image or a photo of your Chili')
