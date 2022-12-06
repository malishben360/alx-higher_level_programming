#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None

    for mx in matrix:
        for i in range(len(mx)):
            print("{:d}".format(mx[i]), end="")
            if i < len(mx) - 1:
                print(" ", end="")
        print("")
