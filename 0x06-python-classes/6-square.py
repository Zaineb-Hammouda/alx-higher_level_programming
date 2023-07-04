#!/usr/bin/python3
""" class square  that defines a square"""


class Square:
    """ class that defines a square by:
    private instance attribute:
        size
    """

    def __init__(self, size=0, position=(0, 0)):
        """creates instance of square with argument size"""
        self.__size = size
        self.__position = position

    def area(self):
        """ returns area of the square """
        return self.__size ** 2

    def my_print(self):
        """ prints the square with the char '#' """
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
