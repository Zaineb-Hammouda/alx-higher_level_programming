#!/usr/bin/python3
"""
4-print_square module
contains the function print_square()
"""


def print_square(size):
    """
    prints a square with the char '#'
    size: the size of the square
    """
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError('size must be an integer')
    if size < 0:
        if type(size) is float:
            raise TypeError('size must be an integer')
        raise ValueError('size must be >= 0')
    if size >= 0:
        for i in range(int(size)):
            print('#' * int(size))
