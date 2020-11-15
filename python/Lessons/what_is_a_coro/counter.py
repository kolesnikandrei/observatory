from random import randint


def counter(start=0, limit=10):
    value = start
    while value < limit:
        value += yield value
    yield value


def main():
    gen = counter()
    gen.send(None)  # prime the generator
    while True:
        value = randint(1, 3)
        total = gen.send(value)
        print(f"sent {value}, got {total}")


main()
