#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    unique_list = set(my_list)
    for i in unique_list:
        res += i
    return res
