
def square(x: int) -> int:
    return x * x


def main():
    result = square(4)
    print(result)  # 16


from dis import dis
print("square: ")
dis(square)
print("main: ")
dis(main)
