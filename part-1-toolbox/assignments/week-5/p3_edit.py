# python3


def editing_distance(seq_a, seq_b):
    """
    Compute editing distance between `seq_a` and `seq_b`.

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

    return dist[len(seq_a)][len(seq_b)]


if __name__ == '__main__':
    str_a = input()
    str_b = input()

    print(editing_distance(str_a, str_b))
