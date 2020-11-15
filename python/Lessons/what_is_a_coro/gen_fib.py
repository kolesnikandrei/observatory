
def fib(count: int):
    a, b = 1, 0
    for _ in range(count):
        a, b = b, a + b
        yield b


def main():
    gen = fib(5)
    print(gen)
    while True:
        print(next(gen))


if __name__ == '__main__':
    main()
