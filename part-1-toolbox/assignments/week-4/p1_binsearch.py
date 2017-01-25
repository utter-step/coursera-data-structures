# python3


def binary_search(array, item):
    """
    Binary search realization.

    >>> binary_search([1, 2, 3, 4], 2)
    1

    >>> binary_search([1, 2, 3, 4], 6)
    -1
    """
    l, r = 0, len(array) - 1

    while l <= r:
        mid = (l + r) // 2

        if array[mid] < item:
            l = mid + 1
        elif array[mid] > item:
            r = mid - 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    n, *array = map(int, input().split())
    k, *lookups = map(int, input().split())

    results = map(lambda lookup: str(binary_search(array, lookup)), lookups)

    print(" ".join(results))
