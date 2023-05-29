#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    length = 0
    for i in my_list:
        length += 1

    for i in my_list:
        if j <= x - 1:
            try:
                print("{:d}".format(i), end="")
            except (ValueError, TypeError):
                pass
            else:
                j += 1
    if x > length:
        raise IndexError('list index out of range')
    print()
    return j
