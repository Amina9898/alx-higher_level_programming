#!/usr/bin/python3
import random
number = random.randint(-10, 10)

print("{} ".format(number), end="")

# if the number is greater than 0
if number > 0:
    print("is positive")

# if the number is 0
elif number == 0:
    print("is zero")

# if the number is less than 0
else:
    print("is negative")
