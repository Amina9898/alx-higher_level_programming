#!/usr/bin/python3
def uppercase(str):
    # Iterate through the string
    for c in str:

    # Convert each letter to its ASCII value
        c = ord(c)

    # Subtract 32 to get the upper-case letter ASCII value
        if 97 <= c <= 122:
            c = c - 32

    # Convert back to a charecter
        c = chr(c)

    # Return the string in uppercase
        print("{}".format(c), end="")
    print()
