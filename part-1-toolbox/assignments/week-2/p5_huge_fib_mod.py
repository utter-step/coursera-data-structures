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


def get_remainder(n, mod):
    """
    Find Fib(n) mod m by computing Pisano period.

    >>> get_remainder(1, 239)
    1

    >>> get_remainder(239, 1000)
    161

    >>> get_remainder(2816213588, 30524)
    10249
    """
    period = get_period(mod)
    return period[n % len(period)]


if __name__ == '__main__':
    n, m = map(int, input().split())

    print(get_remainder(n, m))
