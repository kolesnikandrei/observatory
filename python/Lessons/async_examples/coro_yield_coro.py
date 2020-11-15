
import time

from loop2 import wait


def sleep(duration: float):
    print('(1)in sleep')
    now = time.time()
    threshold = now + duration
    while now < threshold:
        print('(1)inside while in sleep before yield')
        yield
        print('(1)inside while in sleep after yield')
        now = time.time()
    print('(1)out sleep')


def bar():
    print('(1)in bar')
    yield from sleep(0.00005)
    print('(1)out bar')
    return 123


def foo():
    print('(1)in foo')
    value = yield from bar()
    print('(1)out foo')
    return value


def sleep2(duration: float):
    print('(2)in sleep2')
    now = time.time()
    threshold = now + duration
    while now < threshold:
        print('(2)inside while in sleep2 before yield')
        yield
        print('(2)inside while in sleep2 after yield')
        now = time.time()
    print('(2)out sleep')


def bar2():
    print('(2)in bar2')
    yield from sleep2(0.00005)
    print('(2)out bar2')
    return 123


def foo2():
    print('(2)in foo2')
    value = yield from bar2()
    print('(2)out foo2')
    return value


def main():
    tasks = [foo(), foo2()]
    print(wait(tasks))


main()
