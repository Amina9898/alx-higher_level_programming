#!/usr/bin/python3
def islower(c):
    # convert c into its ASCII value
    c = ord(c)

    # If c is from 97 to 122 c return true
    if c >= 97 and c <= 122:
        return True

    # Return False otherwise
    else:
        return False
