#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mx = list(map((lambda mx: list(map((lambda x: x**2), mx))), matrix))
    return new_mx
