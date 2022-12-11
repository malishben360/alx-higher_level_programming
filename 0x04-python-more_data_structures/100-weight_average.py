#!/usr/bin/python3

def weight_average(my_list=[]):
    weight_mul = 0
    weight_sum = 0
    if my_list is None or len(my_list) < 1:
        return 0

    for tup in my_list:
        weight_mul += tup[0] * tup[1]
        weight_sum += tup[1]

    return weight_mul / weight_sum
