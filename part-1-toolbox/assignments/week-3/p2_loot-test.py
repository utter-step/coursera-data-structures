from p2_loot import max_fractional_knapsack_price


def test_knapsack(input_, expected):
    """Test max fractional knapsack solver."""
    _, capacity, items = input_
    guess = max_fractional_knapsack_price(capacity, items)

    if "{0:.4f}".format(guess) == expected:
        print("[*] OK")
    else:
        print("[!] Fail. Expected {0}, got {1}".format(expected, guess))

# Test given inputs
testcase_1 = ((
    3, 50, (
        (60, 20),
        (100, 50),
        (120, 30),
    )
), "180.0000")
testcase_2 = ((
    1, 10, (
        (500, 30),
    )
), "166.6667")

test_knapsack(*testcase_1)
test_knapsack(*testcase_2)

# TODO: some integration tests
