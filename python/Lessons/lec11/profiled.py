"""Project Euler problem 3 solve
    Простые делители числа 13195 — это 5, 7, 13 и 29.
    Какой самый большой делитель числа 600851475143, являющийся простым числом?
"""

import math
import sys
# from memory_profiler import profile
import time


def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if not num % i:
            return False
    return True

# @profile
def find_prime_factors(num):
    """Find prime factors of num"""
    result = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if is_prime(i) and not num % i:
        # if not num % i and is_prime(i):
            result.append(i)
    if is_prime(num):
        result.append(i)
    return result


if __name__ == '__main__':
    try:
        num = int(sys.argv[1])
    except (TypeError, ValueError, IndexError):
        sys.exit("Usage: number")
    if num < 1:
        sys.exit("Error: number must be greater than zero")

    # start = time.time()
    prime_factors = find_prime_factors(num)
    # print(time.time() - start)
    if len(prime_factors) == 0:
        print("Can't find prime factors of %d" % num)
    else:
        print("Answer: %d" % prime_factors[-1])


# python3 -m timeit -n 10 -s'import profiled' 'profiled.find_prime_factors(600851475143)'
