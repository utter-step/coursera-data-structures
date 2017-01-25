# python3
from collections import namedtuple

Item = namedtuple('Item', ['price', 'weight'])


def max_fractional_knapsack_price(capacity, items):
    """
    Solve knapsack problem given the array of items and capacity.

    Items are two-tuples of form (price, weight).
    """
    items = map(lambda item: Item(*item), items)

    total_price = 0
    for price, weight in sorted(items,
                                key=lambda item: item.price / item.weight,
                                reverse=True):
        if capacity > 0:
            value = price / weight
            taking = min(capacity, weight)
            total_price += value * taking
            capacity -= taking
        else:
            break

    return total_price


def main():
    items_count, capacity = map(int, input().split())
    items = [map(int, input().split()) for _ in range(items_count)]

    max_price = max_fractional_knapsack_price(capacity, items)
    print("{0:.4f}".format(max_price))


if __name__ == '__main__':
    main()
