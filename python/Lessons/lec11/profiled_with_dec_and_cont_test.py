"""Collect profiling statistic into graphite"""

from profiled import find_prime_factors
from profiled_with_cont import Stats
from profiled_dec import stats


if __name__ == "__main__":
    with Stats('find_prime_factors'):
        # find_prime_factors(13195)
        find_prime_factors(600851475143)


    @stats('find_prime_factors')
    def test():
        return find_prime_factors(600851475143)


    test()


    def test_2():
        with Stats('find_prime_factors'):
            # find_prime_factors(13195)
            find_prime_factors(600851475143)


    test_2()

