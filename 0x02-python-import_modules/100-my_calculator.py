#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit(0)

length = len(argv)
if length != 4:
    print("Usage: {} <a> <operator> <b>".format(argv[0]))
    exit(1)

op = argv[2]
if op != '+' and op != '-' and op != '*' and op != '/':
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

def calc(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    else:
        return div(a, b)


a = int(argv[1])
b = int(argv[3])
print("{} {} {} = {}".format(a, op, b, calc(a, b, op)))
