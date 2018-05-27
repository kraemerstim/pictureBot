#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import configparser

def get_file_path(file_path):
  return os.path.join(os.path.dirname(__file__), file_path)
    
def set_ini_file(file_path='config.ini'):
  if os.path.isfile(get_file_path(file_path)):
    config.read(os.path.join(os.path.dirname(__file__), file_path))
  
def initialize():
  global config
  config = configparser.ConfigParser()
  set_ini_file()

def get_ini_value(section, key):
  return config.get(section, key, fallback='')
