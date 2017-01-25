# python3
import itertools


def max_pairwise_product(numbers):
    """
    Find max pairwise product.

    Given a sequence of non-negative (important!) integers,
    find the maximum pairwise product, that is,
    the largest integer that can be obtained by multiplying
    two different elements from the sequence.

    Sequence must contain at least two numbers.
    """
    first, second = itertools.islice(a, 2)

    max_first, max_second = max(first, second), min(first, second)

    for el in a:
        if el > max_first:
            max_second = max_first
            max_first = el
        elif el > max_second:
            max_second = el

    return max_first * max_second

n = input()
a = map(int, input().split())

print(max_pairwise_product(a))
