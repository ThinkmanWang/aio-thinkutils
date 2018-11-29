# -*- coding: UTF-8 -*-

import sys
import os

import tornado
import asyncio
import tornado.platform.asyncio

from echoserver.MyEchoServer import MyTorEchoServer

if __name__ == '__main__':
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    ioloop = asyncio.get_event_loop()

    server = MyTorEchoServer()
    server.listen(9000)

    print("Starting server on tcp://localhost:9000")
    ioloop.run_forever()