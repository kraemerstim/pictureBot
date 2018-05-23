#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
import time
import os
import telegramBot
import configreader
import database

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
    picturePath = configreader.getIniValue('Main', 'pictureFolder')
    path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(path, picturePath)

    dbFile = configreader.getIniValue('Main', 'database')
    db = database.DBConnector(dbFile)
    db.initialize

    botToken = configreader.getIniValue('Main', 'botToken')
    telegramBot.TelegramBot(botToken, path)

def main():
    initialize()
    while program_running:
        time.sleep(2)

if __name__ == '__main__':
    main()