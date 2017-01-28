# python3
from collections import deque


def process_packets(packets, buff_size):
    """
    Process given packets.

    For each packet return at what time it started processing
    or -1, if dropped.
    """
    finish_times = deque()
    times = []

    for arrival, processing_time in packets:
        while finish_times and finish_times[0] <= arrival:
            finish_times.popleft()

        if not finish_times:
            finish_times.append(arrival + processing_time)

            times.append(arrival)
            continue

        if len(finish_times) == buff_size:
            times.append(-1)
        else:
            last_finish_time = finish_times[-1]
            finish_times.append(last_finish_time + processing_time)
            times.append(last_finish_time)

    return times


if __name__ == '__main__':
    S, n = map(int, input().split())
    packets = [list(map(int, input().split())) for _ in range(n)]

    times = process_packets(packets, S)

    for time in times:
        print(time)
