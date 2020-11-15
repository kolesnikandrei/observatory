import time
from loop2 import wait


def sleep(duration: float):
    now = time.time()
    threshold = now + duration
    while now < threshold:
        yield
        now = time.time()


def bar():
    yield from sleep(0.1)
    return 123


def foo():
    value = yield from bar()
    return value


def main():
    tasks = [foo(), foo()]
    print(wait(tasks))

main()
