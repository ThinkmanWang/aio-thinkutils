import pymysql
from DBUtils.PooledDB import PooledDB

from thinkutils.config.Config import *

class ThinkMysql:
    g_conn_pool = None

    @classmethod
    def get_default_conn_pool(cls):
        if cls.g_conn_pool is None:
            cls.g_conn_pool = PooledDB(pymysql
                              , mincached = int(ThinkConfig.get_default_config().get("mysql", "maxconnections")) / 2
                              , maxcached = int(ThinkConfig.get_default_config().get("mysql", "maxconnections"))
                              , host=ThinkConfig.get_default_config().get("mysql", "host")
                              , user=ThinkConfig.get_default_config().get("mysql", "user")
                              , passwd=ThinkConfig.get_default_config().get("mysql", "password")
                              , db=ThinkConfig.get_default_config().get("mysql", "db")
                              , port=int(ThinkConfig.get_default_config().get("mysql", "port"))
                              , maxconnections=int(ThinkConfig.get_default_config().get("mysql", "maxconnections"))
                              , charset = "utf8"
                              , use_unicode = True)

        return cls.g_conn_pool

