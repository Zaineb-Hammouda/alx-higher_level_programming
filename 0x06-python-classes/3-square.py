#!/usr/bin/python3
""" class square  that defines a square"""


class Square:
    """ class that defines a square by:
    private instance attribute:
        size
    """
    def __init__(self, size=0):
        """creates instance of square with argument size"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
