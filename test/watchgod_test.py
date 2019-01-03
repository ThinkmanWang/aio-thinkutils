# -*- coding: UTF-8 -*-

import sys
import os

import asyncio
from watchgod import awatch
from watchgod import Change

async def file_monitor():
    async for changes in awatch("/Users/wangxiaofeng/Github-Thinkman/Tornado5Test"):
        for change in changes:
            nType, szPath = change
            print(nType)
            print(szPath)

            if Change.added == nType:
                print("added")
            elif Change.deleted == nType:
                print("deleted")
            elif Change.modified == nType:
                print("modified")

def main():
    loop = asyncio.get_event_loop()

    asyncio.gather(file_monitor())

    loop.run_forever()

if __name__ == '__main__':
    main()