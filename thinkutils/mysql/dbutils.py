import pymysql
from DBUtils.PooledDB import PooledDB

from thinkutils.config.Config import *

class ThinkMysql:
    g_conn_pool = None

    @classmethod
    def get_default_conn_pool(cls):
        if cls.g_conn_pool is None:
            cls.g_conn_pool = PooledDB(pymysql
                              , mincached = int(ThinkConfig.get_default_config().get_int("mysql", "maxconnections") / 2)
                              , maxcached = int(ThinkConfig.get_default_config().get_int("mysql", "maxconnections"))
                              , host=ThinkConfig.get_default_config().get("mysql", "host")
                              , user=ThinkConfig.get_default_config().get("mysql", "user")
                              , password=ThinkConfig.get_default_config().get("mysql", "password")
                              , db=ThinkConfig.get_default_config().get("mysql", "db")
                              , port=int(ThinkConfig.get_default_config().get("mysql", "port"))
                              , maxconnections=int(ThinkConfig.get_default_config().get("mysql", "maxconnections"))
                              , charset = "utf8"
                              , use_unicode = True)

        return cls.g_conn_pool

# def main():
#     conn = ThinkMysql.get_default_conn_pool().connection()
#     cur = conn.cursor(pymysql.cursors.DictCursor)
#     try:
#         cur.execute("SELECT 1")
#         rows = cur.fetchall()
#
#         print("rows count: ", len(rows))
#         row = rows[0]
#
#         print("return: ", row)
#     except Exception as e:
#         pass
#     finally:
#         cur.close()
#
# if __name__ == '__main__':
#     main()