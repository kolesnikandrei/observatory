
def add_this(a, b):
    return a + b


print(add_this(1, 5))
print(add_this("a", "b"))

print('--------------------------')


def add_this(a: int, b: int) -> int:
    return a + b


print(add_this(1, 4))

print('--------------------------')
