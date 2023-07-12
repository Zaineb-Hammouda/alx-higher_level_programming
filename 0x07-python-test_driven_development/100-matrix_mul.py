#!/usr/bin/python3
"""
the 100-matrix_mul module
contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """
    multplies 2 matrices
    m_a and m_b are lists of lists of integers or floats
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    size1 = None
    if m_a == []:
        raise ValueError("m_a can't be empty")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("m_a should contain only integers or floats")
        if size1 is None:
            size1 = len(i)
            if size1 == 0:
                raise ValueError("m_a can't be empty")
        elif size1 != len(i):
            raise TypeError("each row of m_a must be of the same size")

    size2 = None
    if m_b == []:
        raise ValueError("m_b can't be empty")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("m_b should contain only integers or floats")
        if size2 is None:
            size2 = len(i)
            if size2 == 0:
                raise ValueError("m_b can't be empty")
        elif size2 != len(i):
            raise TypeError("each row of m_b must be of the same size")
    if size1 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix = []
    for i in range(len(m_a)):
        mul_list = []
        for j in range(size1):
            mul = 0
            for k in range(size2):
                mul += m_a[i][k] * m_b[k][j]
            mul_list.append(mul)
        matrix.append(mul_list)
    return matrix
