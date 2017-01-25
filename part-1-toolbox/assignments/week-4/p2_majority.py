# python3


def _majority(arr, l, r):
    if l == r:
        return arr[l]

    m = (l + r) // 2
    l_res = _majority(arr, l, m)
    r_res = _majority(arr, m + 1, r)

    count_l = 0
    count_r = 0

    for el in arr[l:r + 1]:
        if el == l_res:
            count_l += 1
        elif el == r_res:
            count_r += 1

    if count_l > (r - l + 1) // 2:
        return l_res
    elif count_r > (r - l + 1) // 2:
        return r_res
    else:
        return -1


def majority(arr):
    """
    Find most frequent item in array, recursive "divide-and-conquer" approach.

    >>> majority([1, 2, 3, 4])
    -1

    >>> majority([2, 3, 9, 2, 2])
    2

    >>> majority([1, 2, 3, 1])
    -1
    """
    return _majority(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    n = input()
    votes = list(map(int, input().split()))

    res = majority(votes)

    if res != -1:
        print(1)
    else:
        print(0)
