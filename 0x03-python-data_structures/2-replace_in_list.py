#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    length = len(my_list)

    if idx < 0:

        return my_list

    elif idx > length:

        return my_list

    else:

        for i in range(0, length):

            if i == idx:

                my_list[i] = element

                return my_list