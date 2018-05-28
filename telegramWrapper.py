#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telepot
import os
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


class TelegramWrapper:

    def __init__(self, token, picture_path = None):
        if picture_path == None:
            picture_path = os.path.abspath(os.path.dirname(__file__))
        self.picture_path = picture_path
        self.TOKEN = token
        self.picture_path = picture_path
        self.bot = telepot.Bot(token)

    def start(self, chat_callback, query_callback):
        self.chat_callback = chat_callback
        self.query_callback = query_callback
        MessageLoop(self.bot, {'chat': self.handle_chat_message, 'callback_query': self.handle_callback_query}).run_as_thread()

    def download_picture(self, file_id):
        os.makedirs(self.picture_path, exist_ok=True)
        path = os.path.join(self.picture_path, file_id) + '.jpg'
        self.bot.download_file(file_id, path)

    def handle_chat_message(self, msg):
        self.chat_callback(msg)
    
    def handle_callback_query(self, msg):
        self.query_callback(msg)

    def send_inline_keyboard(self, chat_id, message):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Press me', callback_data='press')],
        ])

        self.bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)
    
    def send_message(self, chat_id, message):
        self.bot.sendMessage(chat_id, message)

    def answer_callback_query(self, query_id, text):
        self.bot.answerCallbackQuery(query_id, text=text)
