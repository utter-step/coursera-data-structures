# python3


def apply_op(a, b, op):
    """
    Apply binary operation (+, - and * are supported) to operands.

    >>> apply_op(1, 5, '-')
    -4

    >>> apply_op(1, 5, '+')
    6

    >>> apply_op(2, 6, '*')
    12
    """
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b

    raise ValueError('unknown op:', op)


def min_and_max(i, j, ops, mins, maxs):
    """Find min and max values for this operations subtree."""
    min_ = 2 ** 31
    max_ = -2 ** 31

    for k in range(i, j):
        op = ops[k]

        a = apply_op(maxs[i][k], maxs[k + 1][j], op)
        b = apply_op(maxs[i][k], mins[k + 1][j], op)
        c = apply_op(mins[i][k], mins[k + 1][j], op)
        d = apply_op(mins[i][k], maxs[k + 1][j], op)

        min_ = min(a, b, c, d, min_)
        max_ = max(a, b, c, d, max_)

    return min_, max_


def maximize_arithmetic_value_parsed(numbers, ops):
    """
    Maximize value of parsed arithmetic expression by adding parthenses.

    >>> maximize_arithmetic_value_parsed([1], [])
    1

    >>> maximize_arithmetic_value_parsed([6, 4], ['+'])
    10
    """
    maxs = [
        [0 for _ in range(len(numbers))] for _ in range(len(numbers))
    ]
    mins = [
        [0 for _ in range(len(numbers))] for _ in range(len(numbers))
    ]

    for i, number in enumerate(numbers):
        maxs[i][i] = mins[i][i] = number

    n = len(numbers)

    for s in range(n):
        for i in range(n - s):
            j = i + s

            if i == j:
                mins[i][j] = maxs[i][j] = numbers[i]
            else:
                mins[i][j], maxs[i][j] = min_and_max(i, j, ops, mins, maxs)

    return maxs[0][n - 1]


def maximize_arithmetic_value(expr):
    """
    Maximize arithmetic value of given string expression.

    >>> maximize_arithmetic_value('1+5')
    6

    >>> maximize_arithmetic_value('5-8+7*4-8+9')
    200
    """
    numbers = []
    ops = []

    for c in expr:
        if c.isdigit():
            numbers.append(int(c))
        else:
            ops.append(c)

    return maximize_arithmetic_value_parsed(numbers, ops)


if __name__ == '__main__':
    expr = input()

    print(maximize_arithmetic_value(expr))
