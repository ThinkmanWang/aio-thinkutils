# -*- coding: UTF-8 -*-

import sys
import os
import asyncio
import aiohttp

from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError
from tornado import gen

from Constants import *

class TCPConnection(object):

    def __init__(self, stream, address):
        self.__stream = stream
        self.__address = address

        self.__stream.set_close_callback(self.on_close)
        self.on_connect()

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def get_ip(self):
        await asyncio.sleep(20)
        async with aiohttp.ClientSession() as session:
            html = await self.fetch(session, 'http://ip.cn')
            return html

    @gen.coroutine
    def on_close(self):
        if self.__stream is not None and False == self.__stream.closed():
            self.__stream.close()
            self.__stream = None

    @gen.coroutine
    def on_connect(self):

        try:
            szData = yield self.__stream.read_until(EOF)

            yield self.__stream.write(szData.replace(EOF, "".encode(ENCODING)))

            szIP = yield self.get_ip()
            yield self.__stream.write(szIP.encode(ENCODING))
            yield self.__stream.write(b'hehe')
            yield self.__stream.write('hehe'.encode(ENCODING))
            yield self.__stream.write(EOF)

        except Exception as e:
            pass

        if self.__stream is not None and False == self.__stream.closed():
            self.on_connect()

class MyTorEchoServer(TCPServer):

    @gen.coroutine
    def handle_stream(self, stream, address):
        TCPConnection(stream, address)

