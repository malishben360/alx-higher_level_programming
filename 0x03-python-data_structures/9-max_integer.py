#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None:
        return None

    max_x = 0
    for x in my_list:
        if x > max_x:
            max_x = x
    return max_x
