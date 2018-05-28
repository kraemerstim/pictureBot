#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
import time
import os
import telegramWrapper
import configreader
import database
import pictureBot

def cleanup(signal,frame):
    global program_running
    print('Ctrl+C captured, ending read.')
    program_running = False

def initialize():
    global program_running
    program_running = True
    
    # hook fuer ctrl+c    
    signal.signal(signal.SIGINT, cleanup)
    
    configreader.initialize()
    picture_path = configreader.get_ini_value('Main', 'pictureFolder')
    picture_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), picture_path)

    db_file = configreader.get_ini_value('Main', 'database')
    db = database.DBConnector(db_file)
    db.initialize

    bot_token = configreader.get_ini_value('Main', 'botToken')
    telegram_api = telegramWrapper.TelegramWrapper(bot_token, picture_path)

    pictureBot.pictureBot(telegram_api)


def main():
    initialize()
    while program_running:
        time.sleep(2)

if __name__ == '__main__':
    main()
