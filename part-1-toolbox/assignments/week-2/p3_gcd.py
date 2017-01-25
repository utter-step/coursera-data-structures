# python3


def gcd(a, b):
    """Compute GCD using Eucledian algoritm."""
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    a, b = map(int, input().split())

    # it's better if a > b
    if a < b:
        a, b = b, a
    print(gcd(a, b))
