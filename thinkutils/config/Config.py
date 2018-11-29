# -*- coding: UTF-8 -*-

import sys
import os

import configparser

from thinkutils.common_utils.singleton import Singleton

@Singleton
class ThinkConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def read(self, szPath):
        self.config.read(szPath)

    def get(self, szSection, szOption, szDefault = None):
        try:
            return self.config.get(szSection, szOption)
        except Exception as e:
            return szDefault

    def get_boolean(self, szSection, szOption, default = False):
        try:
            return self.config.getboolean(szSection, szOption)
        except Exception as e:
            return default

    def get_int(self, szSection, szOption, default = -1):
        try:
            return self.config.getint(szSection, szOption)
        except Exception as e:
            return default

    def get_float(self, szSection, szOption, default = 0.0):
        try:
            return self.config.getfloat(szSection, szOption)
        except Exception as e:
            return default

# if __name__ == '__main__':
#     config = ThinkConfig.instance()
#     config.read(os.path.dirname(os.path.abspath(__file__)) + "/app.properties")
#
#     print(config.get("mysql", "host"))