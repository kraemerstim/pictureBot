#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

class DBConnector:
    def __init__(self, db_file_name):
        self.conn = sqlite3.connect(db_file_name)
        self.initialize()

    def initialize(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users  
                     (telegramID text NOT NULL UNIQUE, name text)''')
        c.execute('''CREATE TABLE IF NOT EXISTS chilis (
        userid integer NOT NULL,
        name text NOT NULL,
        comment text,
        location text,
        FOREIGN KEY (userid) REFERENCES users(rowid)
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS pictures (
        chiliid integer NOT NULL,
        filename text NOT NULL UNIQUE,
        timestamp text,
        comment text,
        FOREIGN KEY (chiliid) REFERENCES chilis(rowid)
        )''')
        c.close()
        self.conn.commit()

    def getRowIDFromTelegramID(self, telegram_id):
        c = self.conn.cursor()
        c.execute('Select rowid from users where telegramID = ?', (telegram_id,))
        user = c.fetchone()
        if user == None:
            c.execute('Insert into users (telegramID) VALUES (?)', (telegram_id,))
            return c.lastrowid
        return user[0]
