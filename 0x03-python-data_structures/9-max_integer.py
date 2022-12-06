#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    mx_x = 0
    for x in my_list:
        if x > mx_x:
            mx_x = x
    return mx_x
