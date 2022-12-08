#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = list(map((lambda mx: list(map((lambda x: x**2), mx))), matrix))
    return new_matrix
