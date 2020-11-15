import time
import asyncio


def is_prime(x):
    return not any(x // i == x / i for i in range(x - 1, 1, -1))


async def highest_prime_below(x):
    print('Highest prime below %d' % x)
    for y in range(x - 1, 0, -1):
        if is_prime(y):
            print('→ Highest prime below %d is %d' % (x, y))
            return y
#        time.sleep(0.01)
        await asyncio.sleep(0.01)  # blocking func
    return None


async def main():
    t0 = time.time()
    tasks = []
    tasks.append( highest_prime_below(100000))
    tasks.append( highest_prime_below(10000))
    tasks.append( highest_prime_below(1000))

    await asyncio.wait(tasks)

    t1 = time.time()
    print('Took %.2f ms' % (1000 * (t1 - t0)))


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(main())
event_loop.close()