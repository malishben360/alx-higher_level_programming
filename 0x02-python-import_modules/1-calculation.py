#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    import sys
    sys.exit(0)


def comb(opt1, opt2, op, res):
    """Display function
    args:
        opt1: first integer
        opt2: second integer
        op: operator
        res: result of calculation
    Returns:
        Prints and returns nothing.
    """
    print("{} {} {} = {}".format(opt1, op, opt2, res))


a = 10
b = 5
comb(a, b, '+', add(a, b))
comb(a, b, '-', sub(a, b))
comb(a, b, '*', mul(a, b))
comb(a, b, '/', div(a, b))
