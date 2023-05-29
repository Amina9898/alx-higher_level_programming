#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    alist = ""
    for i in (my_list):
        if j <= x:
            j += 1
            try:
                alist += i
            except TypeError:
                alist += str(i)
    print(alist)
    return j
