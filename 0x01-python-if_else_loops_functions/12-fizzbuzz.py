#!/usr/bin/python3

def comb(str):
    print("{} ".format(str), end="")


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            comb("FizzBuzz")
        elif num % 3 == 0:
            comb("Fizz")
        elif num % 5 == 0:
            comb("Buzz")
        else:
            comb(num)
