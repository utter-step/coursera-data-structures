from p1_small_fib import fib_iterative


def fib_naive(n):
    """Naively compute n-th Fibonacci number using recursive technique."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# Test given inputs
print(3, fib_iterative(3) == 2)
print(10, fib_iterative(10) == 55)

# Test range
print("Testing from 0 to 30")
for i in range(31):
    correct = fib_naive(i)
    guess = fib_iterative(i)

    if correct == guess:
        print("OK", i)
    else:
        print("Error! n: {0}, correct: {1}, guess: {2}".format(
            i, correct, guess))
        break
else:
    print("All done")
