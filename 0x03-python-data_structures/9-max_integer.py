#!/usr/bin/python3
def max_integer(my_list=[]):
    i = len(my_list) - 1
    if not my_list:
        return None
    while i > 1:
        j = 0
        while j < i:

            if my_list[j] > my_list[j+1]:
                biggest = my_list[j]
            else:
                biggest = my_list[j+1]
            j += 1
        i -= 1
    return biggest
