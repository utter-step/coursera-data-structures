# python3

NOMINALS = [10, 5, 1]


def change(value):
    """Find minimum number of coins needed to change `value` by NOMINALS."""
    count = 0
    for nominal in NOMINALS:
        count += value // nominal
        value %= nominal

        if value == 0:
            break

    return count


if __name__ == '__main__':
    m = int(input())

    print(change(m))
