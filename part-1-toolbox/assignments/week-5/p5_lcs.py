# python3
# WIP: not finished yet
from functools import reduce


def editing_distance(seq_a, seq_b):
    """
    Compute DP table for editing distance between `seq_a` and `seq_b`.

    >>> editing_distance("ab", "ab")
    0

    >>> editing_distance("short", "ports")
    3

    >>> editing_distance("editing", "distance")
    5

    >>> editing_distance("an", "ab")
    1

    >>> editing_distance("ab", "abba")
    2
    """
    dist = [
        [0 for _ in range(len(seq_b) + 1)] for _ in range(len(seq_a) + 1)
    ]

    for i in range(len(seq_a) + 1):
        dist[i][0] = i
    for j in range(len(seq_b) + 1):
        dist[0][j] = j

    for i in range(1, len(seq_a) + 1):
        for j in range(1, len(seq_b) + 1):
            min_ = dist[i - 1][j - 1]

            if seq_a[i - 1] != seq_b[j - 1]:
                min_ += 1
            if dist[i - 1][j] < min_:
                min_ = dist[i - 1][j] + 1
            if dist[i][j - 1] < min_:
                min_ = dist[i][j - 1] + 1

            dist[i][j] = min_

    return dist


def editing_distance_3(seq_a, seq_b, seq_c):
    """
    Compute DP-table for editing distance between `seq_a` and `seq_b`.

    >>> editing_distance("ab", "ab")[2][2]
    0

    >>> editing_distance("short", "ports")[5][5]
    3

    >>> editing_distance("editing", "distance")[7][8]
    5

    >>> editing_distance("an", "ab")[2][2]
    1

    >>> editing_distance("ab", "abba")[2][4]
    2
    """
    dist = [[
        [0 for _ in range(len(seq_c) + 1)] for _ in range(len(seq_b) + 1)]
        for _ in range(len(seq_a) + 1)
    ]

    for i in range(len(seq_a) + 1):
        dist[i][0][0] = i
    for j in range(len(seq_b) + 1):
        dist[0][j][0] = j
    for k in range(len(seq_c) + 1):
        dist[0][0][k] = k

    for i in range(1, len(seq_a) + 1):
        for j in range(1, len(seq_b) + 1):
            for k in range(1, len(seq_c) + 1):
                min_ = dist[i - 1][j - 1][k - 1] + 1

                if seq_a[i - 1] == seq_b[j - 1] == seq_c[k - 1]:
                    min_ -= 1

                if dist[i - 1][j][k] < min_:
                    min_ = dist[i - 1][j][k] + 1
                if dist[i][j - 1][k] < min_:
                    min_ = dist[i][j - 1][k] + 1
                if dist[i][j][k - 1] < min_:
                    min_ = dist[i][j][k - 1] + 1

                dist[i][j][k] = min_

    return dist


def lcs(seq_a, seq_b):
    """
    Return LCS for two sequences.

    >>> lcs('abba', 'baab')
    ['a', 'b']

    >>> lcs([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7])
    [8, 2, 1, 7]

    >>> lcs('obama', 'baobab')
    ['o', 'b', 'a']

    >>> lcs('harry potter', 'ron weasley')
    ['r', ' ', 'e']
    """
    common = []

    distance = editing_distance(seq_a, seq_b)
    i, j = len(seq_a), len(seq_b)

    while i > 0 and j > 0:
        cur_distance = distance[i][j]

        if distance[i - 1][j] == cur_distance - 1:
            i -= 1
        elif distance[i][j - 1] == cur_distance - 1:
            j -= 1
        else:
            if distance[i - 1][j - 1] == cur_distance:
                common.append(seq_a[i - 1])
            i, j = i - 1, j - 1

    return list(reversed(common))


def lcs3(seq_a, seq_b, seq_c):
    """
    Return LCS for two sequences.

    >>> lcs('abba', 'baab')
    ['a', 'b']

    >>> lcs([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7])
    [8, 2, 1, 7]

    >>> lcs('obama', 'baobab')
    ['o', 'b', 'a']

    >>> lcs('harry potter', 'ron weasley')
    ['r', ' ', 'e']
    """
    common = []

    distance = editing_distance_3(seq_a, seq_b, seq_c)
    i, j, k = len(seq_a), len(seq_b), len(seq_c)

    while i > 0 and j > 0 or k > 0:
        cur_distance = distance[i][j][k]

        if distance[i - 1][j][k] == cur_distance - 1:
            i -= 1
        elif distance[i][j - 1][k] == cur_distance - 1:
            j -= 1
        elif distance[i][j][k - 1] == cur_distance - 1:
            k -= 1
        else:
            if distance[i - 1][j - 1][k - 1] == cur_distance:
                common.append(seq_a[i - 1])
            i, j, k = i - 1, j - 1, k - 1

    return list(reversed(common))


def lcs_many(*seqs):
    """
    Return LCS of arbitary number of sequences.

    >>> len(lcs_many([1, 2, 3], [2, 1, 3], [1, 3, 5]))
    2

    >>> len(lcs_many(
    ...     [8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]))
    3

    >>> lcs_many('haron', 'harry', 'ohara', 'saharra')
    ['h', 'a', 'r']
    """
    return reduce(lcs, seqs)


if __name__ == '__main__':
    n = input()
    seq_a = input().split()
    m = input()
    seq_b = input().split()
    l = input()
    seq_c = input().split()

    print(lcs3(seq_a, seq_b, seq_c))
