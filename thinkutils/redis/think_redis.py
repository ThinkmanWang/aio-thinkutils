#coding=utf-8

import redis

from thinkutils.config.Config import *

class ThinkRedisPool(object):
    g_conn_pool = None

    @classmethod
    def mk_conn_pool(cls
                     , host = '127.0.0.1'
                     , password = None
                     , port = 6379
                     , db = 0
                     , max_connections = 128):
        kwargs = {
            'host': host,
            'port': port,
            'db': db,
            'max_connections': max_connections,
            'password': password,
        }
        _connection_pool = redis.ConnectionPool(**kwargs)

        return _connection_pool

    @classmethod
    def get_default_conn_pool(cls):
        if cls.g_conn_pool is None:
            cls.g_conn_pool = cls.mk_conn_pool(host=ThinkConfig.get_default_config().get("redis", "host")
                                                  , password=ThinkConfig.get_default_config().get("redis", "password")
                                                  , port=ThinkConfig.get_default_config().get("redis", "port")
                                                  , db=ThinkConfig.get_default_config().get("redis", "db"))


# if __name__ == '__main__':
#     connPool1 = ThinkRedisPool.get_default_conn_pool()
#     connPool2 = ThinkRedisPool.get_default_conn_pool()
#
#     print(connPool1 == connPool2)
