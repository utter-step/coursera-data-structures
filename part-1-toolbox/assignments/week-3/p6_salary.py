# python3
from functools import cmp_to_key
from itertools import zip_longest


def compare_for_join(a, b):
    """
    Compare two strings.

    Strings contain numbers,
    we want to select their order to maximize joined value.

    >>> compare_for_join('2', '21')
    1

    >>> compare_for_join('2', '23')
    -1

    >>> compare_for_join('2231', '29')
    -1

    >>> compare_for_join('1110', '111')
    -1

    >>> compare_for_join('111', '111')
    0

    >>> compare_for_join('299', '29')
    1

    >>> compare_for_join('10', '100')
    1

    >>> compare_for_join('59', '599')
    -1
    """
    shortest = min(a, b, key=len)
    fillvalue = shortest[-1]

    for a_char, b_char in zip_longest(a, b, fillvalue=fillvalue):
        if a_char < b_char:
            return -1
        elif a_char > b_char:
            return 1

    ab = a + b
    ba = b + a

    return (ab > ba) - (ab < ba)


def get_salary(numbers):
    """
    Maximize your salary if boss had given you pieces of paper with numbers.

    >>> get_salary(('21', '2'))
    '221'

    >>> get_salary(('9', '4', '6', '1', '9'))
    '99641'

    >>> get_salary(('23', '39', '92'))
    '923923'

    >>> get_salary(('31', '3', '39'))
    '39331'

    >>> get_salary(('29', '299', '3'))
    '329929'

    >>> get_salary(('100', '1000'))
    '1001000'

    >>> get_salary(('59', '599'))
    '59959'

    >>> get_salary(('95', '955'))
    '95955'

    >>> get_salary(('9111', '911', '91'))
    '919119111'

    >>> get_salary(('101', '1011', '1001'))
    '10111011001'

    >>> get_salary(('55', '555', '554'))
    '55555554'

    >>> get_salary(('54321', '543210'))
    '54321543210'

    >>> get_salary(('212', '2122'))
    '2122212'

    >>> get_salary(('121', '1211'))
    '1211211'
    """
    sorted_numbers = sorted(
        numbers, key=cmp_to_key(compare_for_join), reverse=True)

    return "".join(sorted_numbers)


if __name__ == '__main__':
    n = int(input())
    numbers = input().split()

    print(get_salary(numbers))
