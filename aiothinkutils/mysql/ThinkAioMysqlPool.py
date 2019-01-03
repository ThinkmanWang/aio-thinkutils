# -*- coding: UTF-8 -*-

import sys
import os

import asyncio
import aiomysql
from thinkutils.config.Config import *


class ThinkAioMysqlPool(object):
    g_conn_pool = None

    @classmethod
    async def get_default_conn_pool(cls):
        if cls.g_conn_pool is None:
            cls.g_conn_pool = await aiomysql.create_pool(minsize = int(ThinkConfig.get_default_config().get("mysql", "maxconnections")) / 2
                              , maxsize = int(ThinkConfig.get_default_config().get("mysql", "maxconnections"))
                              , host=ThinkConfig.get_default_config().get("mysql", "host")
                              , user=ThinkConfig.get_default_config().get("mysql", "user")
                              , password=ThinkConfig.get_default_config().get("mysql", "password")
                              , db=ThinkConfig.get_default_config().get("mysql", "db")
                              , port=int(ThinkConfig.get_default_config().get("mysql", "port"))
                              , charset = "utf8"
                              , use_unicode = True)

        return cls.g_conn_pool

# async def main():
#     conn_pool = await ThinkAioMysqlPool.get_default_conn_pool()
#     async with conn_pool.acquire() as conn:
#         async with conn.cursor(aiomysql.cursors.DictCursor) as cur:
#             await cur.execute("SELECT 42;")
#             print(cur.description)
#
#             row = await cur.fetchone()
#             print(row)
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())