#!/usr/bin/python3
import re
import sys
import hidden_4

if __name__ != "__main__":
    sys.exit(0)

names = dir(hidden_4)
length = len(names)
for i in range(0, length):
    if names[i][0] != '_':
        print("{}".format(names[i]))
