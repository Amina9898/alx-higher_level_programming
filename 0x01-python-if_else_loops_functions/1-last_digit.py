#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#strip the random number to get to the last digit and print it
last_digit = number % 10
print("{} ".format(last_digit), end="")

# if the last digit is greater than 5
if last_digit > 5:
    print("and is greater than 5")

# if the last digit is 0
elif last_digit == 0:
    print("and is 0")

# if the last digit is less than 6 and not 0
else:
    print("and is less than 6 and not 0")
