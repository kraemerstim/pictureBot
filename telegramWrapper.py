#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telepot
import os
from telepot.loop import MessageLoop

class TelegramWrapper:

    def __init__(self, token, picture_path = None):
        if picture_path == None:
            picture_path = os.path.abspath(os.path.dirname(__file__))
        self.picture_path = picture_path
        self.TOKEN = token
        self.picture_path = picture_path
        self.bot = telepot.Bot(token)

    def start(self, aCallback):
        self.callback = aCallback
        MessageLoop(self.bot, self.handle_message).run_as_thread()

    def download_picture(self, file_id):
        os.makedirs(self.picture_path, exist_ok=True)
        path = os.path.join(self.picture_path, file_id) + '.jpg'
        self.bot.download_file(file_id, path)

    def send_message(self, chat_id, message):
        self.bot.sendMessage(chat_id, message)

    def handle_message(self, msg):
        self.callback(msg)
