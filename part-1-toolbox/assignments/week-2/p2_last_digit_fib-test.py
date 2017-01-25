from p1_small_fib import fib_iterative
from p2_last_digit_fib import fib_last_digit_iterative


def fib_naive(n):
    """Naively compute n-th Fibonacci number using recursive technique."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# Test given inputs
print(3, fib_last_digit_iterative(3) == 2)
print(331, fib_last_digit_iterative(331) == 9)
print(327305, fib_last_digit_iterative(327305) == 5)

# Test simple cases
print("Testing from 0 to 30")
for i in range(31):
    correct = fib_naive(i) % 10
    guess = fib_last_digit_iterative(i)

    if correct == guess:
        print("OK", i)
    else:
        print("Error! n: {0}, correct: {1}, guess: {2}".format(
            i, correct, guess))
        break
else:
    print("All done")

# Test large inputs
low = 300000
high = low + 5
print("Testing from", low, "to", high)
for i in range(low, high):
    correct = fib_iterative(i) % 10
    guess = fib_last_digit_iterative(i)

    if correct == guess:
        print("OK", i, guess)
    else:
        print("Error! n: {0}, correct: {1}, guess: {2}".format(
            i, correct, guess))
        break
else:
    print("All done")
