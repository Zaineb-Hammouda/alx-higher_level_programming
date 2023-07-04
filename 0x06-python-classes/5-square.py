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

    def area(self):
        """ returns area of the square """
        return self.__size ** 2

    def my_print(self):
        """ prints the square with the char '#' """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """ retrieves size """
        return self.__size

    @size.setter
    def size(self, value):
        """raises errors
        property setter for size
        """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
