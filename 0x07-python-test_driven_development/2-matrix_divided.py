#!/usr/bin/python3
"""
2-matrix_divided module
contains the function matrix_divided()
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a function
    matrix: the matrix to divide
    div: the number to divide it by
    """
    if not isinstance(matrix, list):
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    size = None
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')
        if size is None:
            size = len(i)
        elif size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError(
                        'matrix must be a matrix (list of lists) of integers/floats')
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(j / div, 2) for j in i] for i in matrix]
