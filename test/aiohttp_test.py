# -*- coding: UTF-8 -*-

import sys
import os

import asyncio
import aiohttp
from aiohttp_requests import requests
from yarl import URL

async def main():
    resp = await requests.get("http://www.baidu.com")
    szText = await resp.text()

    print(szText)

    url = URL("http://abc.com?a=1&b=2&c=老王")
    print(type(url), url)
    print(url.host)
    print(url.host)
    print(url.query_string)
    print(url.query)
    print(url.query["c"])

asyncio.get_event_loop().run_until_complete(main())
