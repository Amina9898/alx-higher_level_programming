#!/usr/bin/python3
def element_at(my_list, idx):

    length = len(my_list)

    if idx < 0:
        return "None"
    elif idx > length:
        return "None"
    else:
        for i in range(0, length):

            if i == idx:

                return my_list[i]
