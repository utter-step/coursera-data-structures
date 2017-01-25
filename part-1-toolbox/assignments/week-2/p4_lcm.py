# python3
from decimal import Decimal


def gcd(a, b):
    """Compute GCD of two numbers using Eucledian algoritm."""
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    """Compute LCM of two numbers as (a * b) / GCD(a, b)."""
    return int(Decimal(a * b) / gcd(a, b))


if __name__ == '__main__':
    a, b = map(int, input().split())

    # it's better if a > b
    if a < b:
        a, b = b, a
    print(lcm(a, b))
