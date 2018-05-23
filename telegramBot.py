#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telepot
import os
from telepot.loop import MessageLoop

class TelegramBot:

    def __init__(self, token, picture_path = None):
        if picture_path == None:
            picture_path = os.path.abspath(os.path.dirname(__file__))
        self.picture_path = picture_path
        self.TOKEN = token
        self.picture_path = picture_path
        self.bot = telepot.Bot(token)
        MessageLoop(self.bot, self.handleMessage).run_as_thread()

    def download_picture(self, file_id, folder):
        path = os.path.join(self.picture_path, folder)
        os.makedirs(path, exist_ok=True)
        path = os.path.join(path, file_id) + '.jpg'
        self.bot.download_file(file_id, path)

    def handleMessage(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        
        if content_type == 'document' and msg['document']['mime_type'] == 'image/jpeg':
            self.download_picture(msg['document']['file_id'], str(msg['from']['id']))

        elif content_type == 'photo':
            biggestPicture = {'size': -1}
            for photoid in msg['photo']:
                if photoid['file_size'] > biggestPicture['size']:
                    biggestPicture['size'] = photoid['file_size']
                    biggestPicture['id'] = photoid['file_id']
            print (biggestPicture)
            if 'id' in biggestPicture:
                self.download_picture(biggestPicture['id'], str(msg['from']['id']))

        else:
            self.bot.sendMessage(chat_id, 'Hallo ' + msg['from']['first_name'] + ' please send an image or a photo of your Chili')