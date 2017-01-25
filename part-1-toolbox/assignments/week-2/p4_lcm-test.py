import random
from decimal import Decimal

from p4_lcm import lcm


def gcd_naive(a, b):
    """Brute-force GCD computation."""
    best = 1
    for n in range(2, min(a, b) + 1):
        if a % n == 0 and b % n == 0:
            best = n

    return best


def lcm_naive(a, b):
    """LCM computation using naive GCD."""
    return int(Decimal(a * b) / gcd_naive(a, b))


# Test given inputs
print(6, 8, lcm(6, 8) == 24)
print(28851538, 1183019, lcm(28851538, 1183019) == 1933053046)

# Corner-cases
print("Equal", lcm(100, 100) == 100)
print("Equal", lcm(5, 5) == 5)
print("Co-prime", lcm(33, 28) == 33 * 28)
print("Both primes", lcm(13, 17) == 13 * 17)
print("Float round-off errors",
      lcm(226553150, 1023473145) == 46374212988031350)

# Brute-force testing
MAX = 100
TIMES = 10000
for _ in range(TIMES):
    a, b = random.randint(1, MAX), random.randint(1, MAX)
    correct = lcm_naive(a, b)
    guess = lcm(a, b)

    if correct == guess:
        pass
    else:
        print("Error! a, b: {0}, correct: {1}, guess: {2}".format(
            (a, b), correct, guess))
        break
else:
    print("Small correct")

MAX = 1000000
TIMES = 100
for _ in range(TIMES):
    a, b = random.randint(1, MAX), random.randint(1, MAX)
    correct = lcm_naive(a, b)
    guess = lcm(a, b)

    if correct == guess:
        pass
    else:
        print("Error! a, b: {0}, correct: {1}, guess: {2}".format(
            (a, b), correct, guess))
        break
else:
    print("Large correct")
