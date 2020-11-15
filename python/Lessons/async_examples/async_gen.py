import asyncio


async def agen(x):
    for i in range(x):
        print('doing something before yield')
        yield i
        print('doing something after yield')


async def main():
    async for v in agen(37):
        print(v)


asyncio.run(main())
