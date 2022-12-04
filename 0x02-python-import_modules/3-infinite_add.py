#!/usr/bin/python3
from sys import argv, exit

if __name__ != "__main__":
    exit(0)

length = len(argv)
sum_of_args = 0

for i in range(1, length):
    sum_of_args += int(argv[i])
print("{}".format(sum_of_args))
