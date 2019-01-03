# -*- coding: UTF-8 -*-

import sys
import os
import asyncio

from thinkutils.log.log import g_logger

async def test1():
    while True:
        await asyncio.sleep(5)
        g_logger.debug("test1")

async def test2():
    asyncio.gather(test3())
    while True:
        await asyncio.sleep(4)
        g_logger.debug("test2")

async def test3():
    while True:
        await asyncio.sleep(3)
        g_logger.debug("test3")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    asyncio.gather(test1())
    asyncio.gather(test2())

    loop.run_forever()


