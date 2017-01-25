# python3


def compute_table(n):
    """
    Compute DP table for calculating n using `* 2`, `* 3` and `+ 1` operations.

    >>> compute_table(5)
    [0, 0, 1, 1, 2, 3]

    >>> compute_table(10)
    [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]
    """
    table = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ = table[i - 1]
        if i % 2 == 0:
            min_ = min(min_, table[i // 2])
        if i % 3 == 0:
            min_ = min(min_, table[i // 3])
        table[i] = min_ + 1

    return table


def traceback(table):
    """
    Reproduce optimal way to get to the len(table) - 1 using given operations.

    >>> table = compute_table(5)
    >>> traceback(table)
    [5, 4, 3, 1]

    >>> table = compute_table(8)
    >>> traceback(table)
    [8, 4, 2, 1]

    >>> table = compute_table(10)
    >>> traceback(table)
    [10, 9, 3, 1]
    """
    steps = []

    i = len(table) - 1
    while i > 1:
        steps.append(i)
        prev = i - 1

        if i % 2 == 0 and table[i // 2] < table[prev]:
            prev = i // 2
        if i % 3 == 0 and table[i // 3] < table[prev]:
            prev = i // 3

        i = prev

    steps.append(1)
    return reversed(steps)


if __name__ == '__main__':
    n = int(input())

    table = compute_table(n)
    path = traceback(table)

    print(table[n])
    print(" ".join(map(str, path)))
