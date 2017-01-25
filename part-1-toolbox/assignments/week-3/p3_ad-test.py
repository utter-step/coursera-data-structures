from p3_ad import maximize_revenue


def test_maximize_revenue(input_, expected):
    """Test revenue maximization solver."""
    ppcs, clicks = input_
    guess = maximize_revenue(ppcs, clicks)

    if guess == expected:
        print("[*] OK")
    else:
        print("[!] Fail. Expected {0}, got {1}".format(expected, guess))

# Test given inputs
testcase_1 = ((
    (23,),
    (39,),
), 897)
testcase_2 = ((
    (1, 3, -5),
    (-2, 4, 1),
), 23)

test_maximize_revenue(*testcase_1)
test_maximize_revenue(*testcase_2)
