# python3
from math import sqrt


def get_prizes(candies):
    """
    Maximize prize places using given number of candies.

    Best distribution of prizes is: 1, 2, 3, ... n + whats_left.

    So we need to find such n, that (n * (n - 1)) / 2 <= candies.
    Root is 2 * (sqrt(1 + 8 * candies) - 1).

    >>> get_prizes(6)
    [1, 2, 3]

    >>> get_prizes(8)
    [1, 2, 5]

    >>> get_prizes(2)
    [2]

    >>> get_prizes(3)
    [1, 2]

    >>> get_prizes(1)
    [1]

    >>> get_prizes(10)
    [1, 2, 3, 4]

    >>> get_prizes(15)
    [1, 2, 3, 4, 5]

    >>> get_prizes(20)
    [1, 2, 3, 4, 10]
    """
    n = int((sqrt(1 + 8 * candies) - 1) / 2)
    leftover = candies - (n * (n + 1)) // 2

    prizes = [i for i in range(1, n)]
    prizes.append(n + leftover)

    return prizes


if __name__ == '__main__':
    n = int(input())

    prizes = get_prizes(n)

    print(len(prizes))
    print(" ".join(map(str, prizes)))
