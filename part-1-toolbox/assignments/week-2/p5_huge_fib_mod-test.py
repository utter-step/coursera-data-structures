from p5_huge_fib_mod import get_period


def test_get_period():
    period_lengths = [
        1, 3, 8, 6, 20, 24, 16, 12, 24, 60, 10, 24, 28, 48, 40, 24, 36, 24, 18,
        60, 16, 30, 48, 24, 100, 84, 72, 48, 14, 120, 30, 48, 40, 36, 80, 24,
        76, 18, 56, 60, 40, 48, 88, 30, 120, 48, 32, 24, 112, 300, 72, 84, 108
    ]

    for n, period_length in enumerate(period_lengths, start=1):
        computed = get_period(n)
        if len(computed) != period_length:
            print("Error", n, period_length, computed)
    else:
        print("OK, test_get_period")


test_get_period()
