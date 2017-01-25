# python3


def _partition(arr, l, r):
    """
    Split arr[l:r + 1] in two parts, arr[l:j], arr[j:r + 1], return j.

    Every element in arr[l:j] is less or equal to arr[l], every element in
    arr[j:r + 1] is greater or equal to arr[l].

    >>> _partition([2, 20, 1, 3, 5], 0, 4)
    1

    >>> _partition([0, 1, 2, 3, 4], 0, 4)
    0

    >>> _partition([5, 4, 3, 2, 1], 0, 4)
    4

    >>> _partition([1, 0, 1, 0, 2, 1, 1, 5], 0, 7)
    5
    """
    pivot = arr[l]

    j = l
    for i in range(l + 1, r + 1):
        if pivot >= arr[i]:
            arr[i], arr[j + 1] = arr[j + 1], arr[i]
            j += 1

    arr[l], arr[j] = arr[j], arr[l]

    return j


def _partition3(arr, l, r):
    """
    Split arr[l:r + 1] in three parts, return boundaries m1, m2.

    Every element in arr[l:m1] is less then arr[l], every element in
    arr[m1:m2] is equal to arr[l], every element in arr[m2:r + 1] is greater
    than arr[l].

    >>> _partition3([2, 20, 1, 3, 5], 0, 4)
    (1, 1)

    >>> _partition3([0, 1, 2, 3, 4], 0, 4)
    (0, 0)

    >>> _partition3([5, 4, 3, 2, 1], 0, 4)
    (4, 4)

    >>> _partition3([1, 2, 1, 1, 5], 0, 4)
    (0, 2)

    >>> _partition3([1, 0, 1, 0, 2, 1, 1, 5], 0, 7)
    (2, 5)
    """
    pivot = arr[l]

    j = l
    for i in range(l + 1, r + 1):
        if pivot >= arr[i]:
            arr[i], arr[j + 1] = arr[j + 1], arr[i]
            j += 1

    m1 = j

    for i in range(j, l - 1, -1):
        if arr[i] == pivot:
            arr[m1], arr[i] = arr[i], arr[m1]
            m1 -= 1

    return m1 + 1, j


def _quick_sort(arr, l, r):
    if l >= r:
        return

    m = (l + r) // 2
    if arr[l] > arr[r]:
        if arr[l] < arr[m]:
            m = l
    else:
        if arr[r] < arr[m]:
            m = r

    arr[l], arr[m] = arr[m], arr[l]

    m1, m2 = _partition3(arr, l, r)
    _quick_sort(arr, l, m1)
    _quick_sort(arr, m2 + 1, r)

    return arr


def quick_sort(arr):
    """
    Quicksort algorithm (recursive implementation).

    >>> quick_sort([5, 1, 8, 3, 2, 7])
    [1, 2, 3, 5, 7, 8]

    >>> quick_sort([1, 2, 3])
    [1, 2, 3]

    >>> quick_sort([1])
    [1]

    >>> quick_sort([2, 1])
    [1, 2]

    >>> import random
    >>> arr = [random.randrange(0, 10 ** 8) for _ in range(100000)]
    >>> list(sorted(arr)) == quick_sort(arr)
    True
    """
    if len(arr) < 2:
        return arr

    return _quick_sort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    n = input()
    arr = list(map(int, input().split()))

    quick_sort(arr)

    print(" ".join(map(str, arr)))
