#!/usr/bin/python3
"""
0-add_integer module
has one function, add_integer(a, b)
"""


def add_integer(a, b=98):
    """ resturns the sum of two nums """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
