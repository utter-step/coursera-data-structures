# python3
from collections import namedtuple
from operator import attrgetter

Timespan = namedtuple('Timespan', ['from_', 'to'])


def find_suitable_times(tennants_available_timespans):
    """
    Find minimal number of points in time, that you can visit all tennants.

    Input is two-tuples of (from, to).

    1. Order by `to` value.
    2. Start with timespan with lowest `to`, select its `to` point.
    3. Remove all spans including this point.
    4. If any spans left - go to 2.

    >>> find_suitable_times(((1, 3), (2, 5), (3, 5)))
    [3]

    >>> find_suitable_times(((4, 7), (1, 3), (2, 5), (5, 6)))
    [3, 6]
    """
    timespans = map(lambda timespan: Timespan(*timespan),
                    tennants_available_timespans)
    timespans = list(sorted(timespans, key=attrgetter('to')))

    visits = []
    i = 0
    while i < len(timespans):
        time = timespans[i].to
        visits.append(time)
        while (i < len(timespans) and
                timespans[i].from_ <= time <= timespans[i].to):
            i += 1

    return visits


if __name__ == '__main__':
    tennants = int(input())
    timespans = [map(int, input().split()) for _ in range(tennants)]

    solution = find_suitable_times(timespans)
    print(len(solution))
    print(" ".join(map(str, solution)))
