import aiohttp
import asyncio
from aiohttp import request


URLS = ['http://httpbin.org/get', 'http://google.com']


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(URLS[0]) as resp:
            print(resp.status)
            print(await resp.text())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


print('-------------------------------------------')


async def fetch(url: str) -> str:
    async with request("GET", url) as r:
        return await r.text("utf-8")


async def main():
    coros = [fetch(url) for url in URLS]
    results = await asyncio.gather(*coros)
    for result in results:
        print(f"{result}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
