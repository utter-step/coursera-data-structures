# python3


def _compute_discrete_knapsack(items, capacity, max_i, cache):
    if capacity == 0 or max_i == -1:
        return 0

    key = (capacity, max_i)

    if (capacity, max_i) in cache:
        return cache[key]

    w = items[max_i]

    without = _compute_discrete_knapsack(
        items, capacity, max_i - 1, cache)
    with_ = 0
    if w <= capacity:
        with_ = _compute_discrete_knapsack(
            items, capacity - w, max_i - 1, cache) + w

    res = max(with_, without)
    cache[key] = res

    return res


def compute_discrete_knapsack(items, capacity):
    """
    Compute discrete knapsack problem without repetitions.

    The underlying solution uses recursive approach with cache.

    >>> compute_discrete_knapsack([1, 4, 8], 10)
    9

    >>> compute_discrete_knapsack([9, 7, 2, 3, 5, 1], 11)
    11

    >>> compute_discrete_knapsack([15], 11)
    0

    >>> compute_discrete_knapsack([15, 1, 1], 30)
    17

    >>> compute_discrete_knapsack([9, 6, 4, 3], 16)
    16
    """
    cache = {}

    items = list(filter(lambda weight: weight <= capacity, items))

    return _compute_discrete_knapsack(items, capacity, len(items) - 1, cache)


if __name__ == '__main__':
    capacity, n = map(int, input().split())
    items = map(int, input().split())

    print(compute_discrete_knapsack(items, capacity))
