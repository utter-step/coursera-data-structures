from p1_change import change


# Test given inputs
print(2, change(2) == 2)
print(28, change(28) == 6)

# Test some simple values
print(1, change(1) == 1)
print(3, change(3) == 3)
print(5, change(5) == 1)
print(9, change(9) == 5)
print(10, change(10) == 1)
print(11, change(11) == 2)
print(16, change(16) == 3)

# Maybe implement some "try every combination"-solution and test it somewhere
# under 20
