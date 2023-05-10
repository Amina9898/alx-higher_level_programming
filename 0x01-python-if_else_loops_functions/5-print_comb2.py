#!/usr/bin/python3
# loop through the numbers from 0 to 99 and output them
for i in range(0, 100):
    if i != 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{}".format(i))
