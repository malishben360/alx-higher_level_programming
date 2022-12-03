#!/usr/bin/python3

def comb(num1, num2, delim):
    print("{}{}{}".format(num1, num2, delim), end='')


for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            comb(i, j, "\n")
        else:
            comb(i, j, ", ")
