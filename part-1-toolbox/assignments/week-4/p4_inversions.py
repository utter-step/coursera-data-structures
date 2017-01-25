# python3


def merge(arr_a, arr_b):
    """
    Merge two ordered arrays, return merged result and inversions count.

    >>> merge([1, 3, 5], [2, 5, 6])
    ([1, 2, 3, 5, 5, 6], 2)
    """
    res = []
    len_a, len_b = len(arr_a), len(arr_b)
    i, j = 0, 0

    inversions = 0

    while i < len_a and j < len_b:
        a, b = arr_a[i], arr_b[j]
        if a <= b:
            res.append(a)
            i += 1
        else:
            res.append(b)
            j += 1

            inversions += len(arr_a) - i

    res.extend(arr_a[i:])
    res.extend(arr_b[j:])

    i, j = 0, 0

    return res, inversions


def merge_sort_counting(arr):
    """
    Mergesort given array (recursively) and return inversions count.

    >>> merge_sort_counting([2, 3, 9, 2, 9])
    ([2, 2, 3, 9, 9], 2)

    >>> merge_sort_counting([3, 2, 1])
    ([1, 2, 3], 3)

    >>> merge_sort_counting([3, 2, 1, 0])
    ([0, 1, 2, 3], 6)

    >>> merge_sort_counting([5, 1, 8, 3, 2, 7])
    ([1, 2, 3, 5, 7, 8], 7)

    >>> merge_sort_counting([1, 2, 3])
    ([1, 2, 3], 0)

    >>> merge_sort_counting([1])
    ([1], 0)

    >>> import random
    >>> arr = [random.random() for _ in range(100)]
    >>> list(sorted(arr)) == merge_sort_counting(arr)[0]
    True
    """
    if len(arr) == 1:
        return arr, 0

    mid = len(arr) // 2
    left, inversions_l = merge_sort_counting(arr[:mid])
    right, inversions_r = merge_sort_counting(arr[mid:])

    merged, inversions = merge(left, right)

    return merged, inversions + inversions_l + inversions_r


if __name__ == '__main__':
    n = input()
    numbers = list(map(int, input().split()))

    sorted_, inversions = merge_sort_counting(numbers)

    print(inversions)
