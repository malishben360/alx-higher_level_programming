#!/usr/bin/python3

def comb(str):
    print("{} ".format(str), end="")


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            comb("fizzbuzz")
        elif num % 3 == 0:
            comb("fizz")
        elif num % 5 == 0:
            comb("buzz")
        else:
            comb(num)
    comb("$")
