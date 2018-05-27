#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

class DBConnector:
    def __init__(self, aFileName):
        self.conn = sqlite3.connect(aFileName)
        self.initialize()

    def initialize(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users  
                     (telegramID text NOT NULL UNIQUE, name text)''')
        c.execute('''CREATE TABLE IF NOT EXISTS chilis (userid integer NOT NULL,
        name text NOT NULL,
        comment text,
        location text,
        FOREIGN KEY (userid) REFERENCES users(rowid))''')
        c.execute('''CREATE TABLE IF NOT EXISTS pictures (chiliid integer NOT NULL,
        filename text NOT NULL UNIQUE,
        timestamp text,
        comment text,
        FOREIGN KEY (chiliid) REFERENCES chilis(rowid))''')
        c.close()
        self.conn.commit()

    def getRowIDFromTelegramID(self, aTelegramID):
        c = self.conn.cursor()
        c.execute('Select rowid from users where telegramID = ?', (aTelegramID,))
        user1 = c.fetchone()
        if user1 == None:
            c.execute('Insert into users (telegramID) VALUES (?)', (aTelegramID,))
            return c.lastrowid
        return user1[0]