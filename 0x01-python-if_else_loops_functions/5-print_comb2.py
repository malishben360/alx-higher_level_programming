#!/usr/bin/python3

def print_comb(num1, num2, delim):
    print("{}{}{}".format(num1, num2, delim), end='')


for num in range(0, 100):
    if num < 10:
        print_comb(0, num, ", ")
    elif num > 9 and num < 99:
        print_comb(num, ", ", '')
    else:
        print("{}".format(num))
