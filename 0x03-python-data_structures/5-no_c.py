#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    idx = 0
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            new_str += my_string[idx:i]
            idx = i + 1
    new_str += my_string[idx:]
    return new_str
