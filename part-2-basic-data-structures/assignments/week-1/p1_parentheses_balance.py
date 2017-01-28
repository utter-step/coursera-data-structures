# python3


PARENTHESES = {
    '}': '{',
    ']': '[',
    ')': '(',
}
OPENING_PARENTHESES = set(PARENTHESES.values())
CLOSING_PARENTHESES = set(PARENTHESES.keys())


def check_parentheses(string):
    """
    Check parentheses balance in given string. Get first unmatched index or -1.

    Works with `[](){}`.

    >>> check_parentheses("[]")
    -1

    >>> check_parentheses("{}[]")
    -1

    >>> check_parentheses("[()]")
    -1

    >>> check_parentheses("(())")
    -1

    >>> check_parentheses("{[]}()")
    -1

    >>> check_parentheses("{")
    0

    >>> check_parentheses("}))")
    0

    >>> check_parentheses("{[}")
    2

    >>> check_parentheses("foo(bar);")
    -1

    >>> check_parentheses("foo(bar[i);")
    9

    >>> check_parentheses("(((")
    0
    """
    stack = []

    for i, c in enumerate(string):
        if c in OPENING_PARENTHESES:
            stack.append((i, c))
        elif c in CLOSING_PARENTHESES:
            if not stack:
                return i

            _, last = stack.pop()
            if PARENTHESES[c] != last:
                return i

    if stack:
        return stack[0][0]

    return -1


if __name__ == '__main__':
    s = input()

    error_index = check_parentheses(s)
    if error_index != -1:
        print(error_index + 1)
    else:
        print("Success")
