#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

class DBConnector:
    def __init__(self, aFileName):
        self.conn = sqlite3.connect(aFileName)
        self.initialize()

    def initialize(self):
        c = self.conn.cursor()
        c.execute('CREATE Table test (test text)')
        c.close()
        self.conn.commit()
