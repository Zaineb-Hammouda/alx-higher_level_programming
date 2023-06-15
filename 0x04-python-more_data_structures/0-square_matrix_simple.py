#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for sqr in matrix:
        sqr = list(map(lambda n: n**2, sqr))
        new_matrix.append(sqr)
    return new_matrix
