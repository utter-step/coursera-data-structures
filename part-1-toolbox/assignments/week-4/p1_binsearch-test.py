import random

from p1_binsearch import binary_search


MAX = 100


def test_binary_search(size, count):
    """Test binary_search method."""
    array = list(
        sorted([random.randrange(0, min(size + 1, MAX)) for i in range(size)]))
    set_array = set(array)

    for i in range(count):
        needle = random.randrange(0, min(size + 1, MAX))

        guess = binary_search(array, needle)

        assert needle in set_array or guess == -1, (
            "[!] FAIL. Found not existing. {0}, {1}, guess: {2}".format(
                array, needle, guess))

        assert needle not in set_array or guess != -1, (
            "[!] FAIL. Not found. {0}, {1}".format(array, needle))
        assert needle not in set_array or array[guess] == needle, (
            "[!] FAIL. Wrong index. {0}, {1}, guess: {2}".format(
                array, needle, guess))


def test_given():
    """Test on data from assignment."""
    array = [1, 5, 8, 12, 13]
    lookups = [8, 1, 23, 1, 11]

    results = [2, 0, -1, 0, -1]

    for lookup, result in zip(lookups, results):
        assert binary_search(array, lookup) == result


test_binary_search(0, 100)
test_binary_search(1, 100)
test_binary_search(2, 100)
test_binary_search(3, 100)
test_binary_search(4, 100)
test_binary_search(10, 100)
test_binary_search(50, 100)
test_binary_search(100, 100)
test_binary_search(1000, 100)
test_binary_search(10000, 100)
test_binary_search(100000, 100)

test_given()
