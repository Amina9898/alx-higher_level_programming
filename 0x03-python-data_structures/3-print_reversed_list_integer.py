#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    length = len(my_list)

    if length != 0:

        my_list.reverse()

        for i in range(length):

            print("{}".format(my_list[i]))
