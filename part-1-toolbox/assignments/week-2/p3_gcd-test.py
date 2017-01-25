import random
from p3_gcd import gcd


def gcd_naive(a, b):
    """Brute-force GCD computation."""
    best = 1
    for n in range(2, min(a, b) + 1):
        if a % n == 0 and b % n == 0:
            best = n

    return best


# Test given inputs
print(18, 35, gcd(18, 35) == 1)
print(28851538, 1183019, gcd(28851538, 1183019) == 17657)

# Corner-cases
print("Equal", gcd(100, 100) == 100)
print("Equal", gcd(5, 5) == 5)
print("Co-prime", gcd(33, 28) == 1)
print("Both primes", gcd(13, 17) == 1)

# Brute-force testing
MAX = 100
TIMES = 10000
for _ in range(TIMES):
    a, b = random.randint(1, MAX), random.randint(1, MAX)
    correct = gcd_naive(a, b)
    guess = gcd(a, b)

    if correct == guess:
        pass
    else:
        print("Error! a, b: {0}, correct: {1}, guess: {2}".format(
            (a, b), correct, guess))
        break
else:
    print("Small correct")

MAX = 100000
TIMES = 1000
for _ in range(TIMES):
    a, b = random.randint(1, MAX), random.randint(1, MAX)
    correct = gcd_naive(a, b)
    guess = gcd(a, b)

    if correct == guess:
        pass
    else:
        print("Error! a, b: {0}, correct: {1}, guess: {2}".format(
            (a, b), correct, guess))
        break
else:
    print("Large correct")
