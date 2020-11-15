import asyncio


async def foo():
    return 37


def main():
    coro = foo()
    print(coro)
    result = asyncio.run(coro)
    print(result)


main()
