# -*- coding: UTF-8 -*-

import sys
import os

import asyncio
import aioredis
from thinkutils.config.Config import *
from thinkutils.datetime.datetime_utils import *

class ThinkAioRedisPool(object):

    g_conn_pool = None

    @classmethod
    async def mk_conn_pool(cls
                     , host='127.0.0.1'
                     , password=None
                     , port=6379
                     , db=0
                     , max_connections=128):

        szAddress = "redis://{}:{}".format(host, port)
        _conn_pool = await aioredis.create_pool(szAddress, db=db, password=password, minsize=2, maxsize=max_connections)
        return _conn_pool

    @classmethod
    async def get_default_conn_pool(cls):
        if cls.g_conn_pool is None:
            cls.g_conn_pool = await cls.mk_conn_pool(host=ThinkConfig.get_default_config().get("redis", "host")
                                               , password=ThinkConfig.get_default_config().get("redis", "password")
                                               , port=ThinkConfig.get_default_config().get("redis", "port")
                                               , db=ThinkConfig.get_default_config().get_int("redis", "db"))
        return cls.g_conn_pool


# async def main():
#     # conn_pool = await ThinkAioRedisPool.get_default_conn_pool()
#     with await (await ThinkAioRedisPool.get_default_conn_pool()) as conn:
#         await conn.execute('set', 'fxxxxk', get_current_time_str())
#
#         szVal = await conn.execute("get", "fxxxxk")
#         print("return val: ", szVal.decode())
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())