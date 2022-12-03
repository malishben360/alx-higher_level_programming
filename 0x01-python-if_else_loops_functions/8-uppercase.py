#!/usr/bin/python3

def _print(char):
    print("{}".format(char), end="")


def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            _print(chr(ord(char) - 32))
        else:
            _print(char)
    _print('\n')
