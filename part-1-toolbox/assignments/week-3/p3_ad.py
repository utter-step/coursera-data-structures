# python3


def maximize_revenue(ppcs, clicks):
    """
    Maximize ad placing revenue with given PPCs and average clicks.

    Order PPCs and average clicks count, that multiply value-by-value.
    """
    return sum(
        map(lambda aggr: aggr[0] * aggr[1], zip(sorted(ppcs), sorted(clicks))))


if __name__ == '__main__':
    i = input()
    ppcs = map(int, input().split())
    clicks = map(int, input().split())

    print(maximize_revenue(ppcs, clicks))
