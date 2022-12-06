#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    l = 0
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            new_str += my_string[l:i]
            l = i + 1
    new_str += my_string[l:]
    return new_str
