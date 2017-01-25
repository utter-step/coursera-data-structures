# python3


def get_period(mod):
    """
    Find Pisano period for given modulo.

    >>> get_period(6)
    [0, 1, 1, 2, 3, 5, 2, 1, 3, 4, 1, 5, 0, 5, 5, 4, 3, 1, 4, 5, 3, 2, 5, 1]

    >>> get_period(0)
    [0]

    >>> get_period(1)
    [0]

    >>> get_period(2)
    [0, 1, 1]
    """
    if mod < 2:
        return [0]

    a, b = 0, 1
    remainders = []
    for i in range(6 * mod + 3):
        remainders.append(a % mod)
        a, b = b, (a + b) % mod

        if remainders[-2:] == [0, 1] and len(remainders) > 2:
            return remainders[:-2]

    return -1


def get_last_digit_fibsum(n):
    """
    Get last digit of sum(fib(i) for i in range(n + 1)).

    Uses the fact, that this sum is equal to fib(n + 2) - 1.

    >>> get_last_digit_fibsum(3)
    4

    >>> get_last_digit_fibsum(100)
    5
    """
    period = get_period(10)

    return (period[(n + 2) % len(period)] - 1) % 10


def get_last_digit_fibsum_partial(m, n):
    """
    Get last digit of sum(fib(i) for i in range(m, n + 1)).

    >>> get_last_digit_fibsum_partial(3, 7)
    1

    >>> get_last_digit_fibsum_partial(10, 10)
    5

    >>> get_last_digit_fibsum_partial(10, 200)
    2
    """
    return (get_last_digit_fibsum(n) - get_last_digit_fibsum(m - 1)) % 10


if __name__ == '__main__':
    m, n = map(int, input().split())

    print(get_last_digit_fibsum_partial(m, n))
