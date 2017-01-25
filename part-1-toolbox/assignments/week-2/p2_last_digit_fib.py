# python3


def fib_last_digit_iterative(n):
    """
    Use incremental approach to compute last digit in n-th Fibonacci number.

    There is a better approach using matrix multiplication,
    but inputs in this problem are rather low for us not to implement it.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 10

    return a


if __name__ == '__main__':
    n = int(input())

    print(fib_last_digit_iterative(n))
