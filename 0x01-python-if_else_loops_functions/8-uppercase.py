#!/usr/bin/python3

def display(char):
    print("{}".format(char), end="")


def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            display(chr(ord(char) - 32))
        else:
            display(char)
    display('\n')
