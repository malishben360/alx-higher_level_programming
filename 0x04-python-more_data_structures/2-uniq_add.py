#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    uniq_set = set(my_list)
    for x in uniq_set:
        total += x
    return total
