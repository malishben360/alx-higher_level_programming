#!/usr/bin/python3
from sys import argv, exit

if __name__ != "__main__":
    exit(0)

length = len(argv)
if length != 2:
    print("{} arguments{}".format(length - 1, '.' if length == 1 else ':'))
else:
    print("{} argument:".format(length - 1))

for i in range(1, length):
    print("{}: {}".format(i, argv[i]))
